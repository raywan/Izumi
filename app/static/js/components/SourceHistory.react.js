var Hist = React.createClass({
  render: function() {
    var href = '/sources/' + this.props.sourceId.toString()
    return (
      <a href={href}>
        <li className="source-item">
          <p>{this.props.id}</p>
          <p>{this.props.dPath}</p>
          <p>{this.props.dInorg}</p>
          <p>Updated by {this.props.author}</p>
        </li>
      </a>
    );
  }
});

var HistoryBox = React.createClass({
  render: function() {
    var history = []
    this.props.data.forEach(function(h) {
      history.push(
        <Hist
          id={h.id}
          sourceId={h.source_id}
          author={h.author}
          date={h.date_created}
          dPath={h.d_pathogen_pollution}
          dInorg={h.d_inorganic_pollution}
          dOrg={h.d_organic_pollution}
          dMacro={h.d_macroscopic_pollution}
          dTherm={h.d_thermal_pollution}
          dClimate={h.d_climate_condition}
          dDepletion={h.d_depletion_risk}
          dStress={h.d_stress}
       />
      );
    });
    return (
      <div className="history-box">
        Recent Changes
        <ul className="history-list">
          {history}
        </ul>
      </div>
    );
  }
});

var SourceHistory = React.createClass({
  getInitialState: function() {
    return {
      historyData:[]
    };
  },

  loadHistory: function() {
    var url = "http://localhost:8000/api/history?source_id=" + location.pathname.split('/')[2]
    $.ajax({
      type: "GET",
      url: url,
      contentType: "application/json; charset=utf-8",
      dataType: "json",
      success: function(data, status, jqXHR) {
        this.setState({historyData: data});
      }.bind(this),
      error: function(xhr, status, err) {
      }.bind(this)
    });
  },
  componentDidMount: function() {
    this.loadHistory();
    setInterval(this.loadHistory, this.props.pollInterval);
  },
  render: function() {
    return (
      <HistoryBox data={this.state.historyData}/>
    );
  }
});

React.render(<SourceHistory pollInterval={10000}/>, document.querySelectorAll('.source-history')[0])

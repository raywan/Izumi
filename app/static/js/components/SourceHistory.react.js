var Hist = React.createClass({
  render: function() {
    var href = '/sources/' + this.props.sourceId.toString();
    var dateCreated = moment(this.props.dateCreated).format('MMMM Do YYYY, h:mm a');
    var user_href= '/profile/' + this.props.author;
    return (
      <div className="history-item-detail history-item list-group">
        <h4>Date Updated: {dateCreated} by <a href={user_href}>{this.props.author}</a></h4>
        <p className="change-header"><strong>Changes (&#916;):</strong></p>
        <p>Pathogen Pollution: {this.props.dPath}</p>
        <p>Inorganic Pollution: {this.props.dInorg}</p>
        <p>Organic Pollution: {this.props.dOrg}</p>
        <p>Macroscopic Pollution: {this.props.dMacro}</p>
        <p>Thermal Pollution: {this.props.dTherm}</p>
        <p>Climate Condition: {this.props.dClimate}</p>
        <p>Depletion Risk: {this.props.dDepletion}</p>
        <p>Stress: {this.props.dStress}</p>
      </div>
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
          dateCreated={h.date_created}
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
        <h2>Recent Changes</h2>
        {history}
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
    var url = "http://localhost:8000/api/history?sort_date=true&source_id=" + location.pathname.split('/')[2]
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

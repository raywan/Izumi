var Source = React.createClass({
  render: function() {
    var href = '/sources/' + this.props.id.toString()
    return (
      <a href={href}>
        <li className="source-item">
          <p>{this.props.sourceType}</p>
          <p>{this.props.lat}, {this.props.lng}</p>
          <p>Source by {this.props.author}</p>
        </li>
      </a>
    );
  }
});

var Hist = React.createClass({
  render: function() {
    var href = '/sources/' + this.props.sourceId.toString()
    console.log("SDLFKSDF");
    console.log(this.props.lat);
    console.log(this.props.lng);
    return (
      <a href={href}>
        <li className="history-item">
          <p>{this.props.lat}, {this.props.lng}</p>
          <p>{this.props.date}</p>
          <p>Updated by {this.props.author}</p>
        </li>
      </a>
    );
  }
});

var SourceBox = React.createClass({
  render: function() {
    var sources = []
    this.props.data.forEach(function(source) {
      sources.push(
        <Source
          id={source.id}
          lat={source.latitude}
          lng={source.longitude}
          sourceType={source.source_type}
          author={source.author}
        />
      );
    });
    return (
      <div className="source-box">
        List of Sources
        <ul className="source-list">
          {sources}
        </ul>
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
          lat={h.latitude}
          lng={h.longitude}
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

var RecentBox = React.createClass({
  getInitialState: function() {
    return {
      sourceData:[],
      historyData:[]
    };
  },

  loadSources: function() {
    $.ajax({
      type: "GET",
      url: "http://localhost:8000/api/sources?sort_date=true&limit=5",
      contentType: "application/json; charset=utf-8",
      dataType: "json",
      success: function(data, status, jqXHR) {
        this.setState({sourceData: data});
      }.bind(this),
      error: function(xhr, status, err) {
      }.bind(this)
    });
  },
  loadHistory: function() {
    $.ajax({
      type: "GET",
      url: "http://localhost:8000/api/history?sort_date=true&limit=5",
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
    this.loadSources();
    this.loadHistory();
    setInterval(this.loadSources, this.props.pollInterval);
    setInterval(this.loadHistory, this.props.pollInterval);
  },
  render: function() {
    return (
      <div className="recent-content">
        <SourceBox data={this.state.sourceData}/>
        <HistoryBox data={this.state.historyData} />
      </div>
    );
  }
});

React.render(<RecentBox pollInterval={10000}/>, document.querySelectorAll('.recent-container')[0])

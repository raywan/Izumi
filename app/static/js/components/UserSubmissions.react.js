var Source = React.createClass({
  render: function() {
    var href = '/sources/' + this.props.id.toString()
    var dateCreated = moment(this.props.dateCreated).format('MMMM Do YYYY, h:mm:ss a')
    return (
      <div className="source-item list-group">
        <a href={href} class="list-group-item active">
          <h4 className="list-group-item-heading">@{this.props.lat}, {this.props.lng}</h4>
          <p>Type: {this.props.sourceType}</p>
          <p>Date Created: {dateCreated}</p>
          <p>Source by {this.props.author}</p>
        </a>
      </div>
    );
  }
});

var Hist = React.createClass({
  render: function() {
    var href = '/sources/' + this.props.sourceId.toString()
    var dateCreated = moment(this.props.dateCreated).format('MMMM Do YYYY, h:mm:ss a')
    return (
      <div className="source-item list-group">
        <a href={href} class="list-group-item active">
          <h4 className="list-group-item-heading">@{this.props.lat}, {this.props.lng}</h4>
          <p>Date Updated: {dateCreated}</p>
          <p>Update by {this.props.author}</p>
        </a>
      </div>
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
          dateCreated={source.date_created}
          author={source.author}
        />
      );
    });
    return (
      <div className="recent-source-box">
        <h3>Sources Submitted</h3>
        {sources}
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
      <div className="recent-history-box">
        <h3>Changes Submitted</h3>
        {history}
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
    var author = window.location.pathname.split('/')[2]
    var url = "http://localhost:8000/api/history?sort_date=true&limit=5&author=" + author;
    console.log(url);
    $.ajax({
      type: "GET",
      url: url,
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
    var author = window.location.pathname.split('/')[2]
    var url = "http://localhost:8000/api/history?sort_date=true&limit=5&author=" + author;
    console.log(url);
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

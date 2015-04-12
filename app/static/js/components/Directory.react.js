var Source = React.createClass({
  render: function() {
    var href = '/sources/' + this.props.id.toString()
    return (
      <a href={href}>
        <li className="source-item">
          <p>Type: {this.props.sourceType}</p>
          <p>Coordinates: {this.props.lat}, {this.props.lng}</p>
          <p>Last Update: {this.props.lastUpdated}</p>
          <p>Source by {this.props.author}</p>
        </li>
      </a>
    );
  }
});

var SourceBox = React.createClass({
  sortSources: function(sources) {
    if (this.props.sorting === 'lat') {
      sources.sort(function (a, b) {
        if (a.latitude > b.latitude) return 1
        if (a.latitude < b.latitude) return -1
        return 0;
      });
    } else if (this.props.sorting === 'lat_r') {
      sources.sort(function (a, b) {
        if (a.latitude > b.latitude) return -1
        if (a.latitude < b.latitude) return 1
        return 0;
      });
    } else if (this.props.sorting === 'long') {
      sources.sort(function (a, b) {
        if (a.longitude > b.longitude) return 1
        if (a.longitude < b.longitude) return -1
        return 0;
      });
    } else if (this.props.sorting === 'long_r') {
      sources.sort(function (a, b) {
        if (a.longitude > b.longitude) return 1
        if (a.longitude < b.longitude) return -1
        return 0;
      });
    } else if (this.props.sorting === 'stress') {
      sources.sort(function (a, b) {
        if (a.longitude > b.longitude) return 1
        if (a.longitude < b.longitude) return -1
        return 0;
      });
    } else if (this.props.sorting === 'stress_r') {
      sources.sort(function (a, b) {
        if (a.longitude > b.longitude) return 1
        if (a.longitude < b.longitude) return -1
        return 0;
      });
    }
    return sources
  },
  render: function() {
    var sources = []
    var sorted_sources= []
    this.props.data.forEach(function(source) {
      sorted_sources.push(source);
    });
    sorted_sources = this.sortSources(sorted_sources);
    sorted_sources.forEach(function(source) {
      sources.push(
        <Source
          id={source.id}
          author={source.author}
          lastUpdated={source.last_updated}
          lat={source.latitude}
          lng={source.longitude}
          sourceType={source.source_type}
        />
      );
    });
    return (
      <div className="source-box">
        <ul className="source-list">
          {sources}
        </ul>
      </div>
    );
  }
});

var Filter = React.createClass({
  onUserChange: function(event) {
    this.props.handleChange(event.target.value);
  },
  render: function() {

    return (
      <select onChange={this.onUserChange}>
        <option value='none'></option>
        <option value="lat">Latitude</option>
        <option value="lat_r">Latitude - reverse</option>
        <option value="long">Longitude</option>
        <option value="long_r">Longitude - reverse</option>
        <option value="stress">Stress</option>
        <option value="stress_r">Stress - reverse</option>
      </select>
    );
  }

});

var Directory = React.createClass({
  getInitialState: function() {
    return {
      sourceData:[],
      sorting: '',
    };
  },
  loadSources: function() {
    $.ajax({
      type: "GET",
      url: "http://localhost:8000/api/sources?sort_date=true",
      contentType: "application/json; charset=utf-8",
      dataType: "json",
      success: function(data, status, jqXHR) {
        this.setState({sourceData: data});
      }.bind(this),
      error: function(xhr, status, err) {
      }.bind(this)
    });
  },
  componentDidMount: function() {
    this.loadSources();
    setInterval(this.loadSources, this.props.pollInterval);
  },
  handleChange: function(sort_by) {
    this.setState({sorting: sort_by});
  },
  render: function() {
    return (
      <div className="directory">
        <Filter sorting={this.state.sorting} handleChange={this.handleChange}/>
        <SourceBox data={this.state.sourceData} sorting={this.state.sorting}/>
      </div>
    );
  }
});

React.render(<Directory pollInterval={30000}/>, document.querySelectorAll('.content')[0])

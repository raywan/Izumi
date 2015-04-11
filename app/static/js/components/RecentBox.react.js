var Source = React.createClass({
  render: function() {
    return (
      <li className="source-item">
        I'm a Source
      </li>
    );
  }
});

var Event = React.createClass({
  render: function() {
    return (
      <li className="event-item">
        I'm an Event
      </li>
    );
  }
});

var SourceBox = React.createClass({
  render: function() {
    return (
      <div className="source-box">
        List of Sources
        <ul className="source-list">
          <Source/>
          <Source/>
          <Source/>
        </ul>
      </div>
    );
  }
});

var EventBox = React.createClass({
  render: function() {
    return (
      <div className="event-box">
        List of Events
        <ul className="event-list">
          <Event/>
          <Event/>
          <Event/>
        </ul>
      </div>
    );
  }
});

var RecentBox = React.createClass({
  render: function() {
    return (
      <div className="recent-content">
        <SourceBox/>
        <EventBox/>
      </div>
    );
  }
});

React.render(<RecentBox/>, document.querySelectorAll('.recent-container')[0])

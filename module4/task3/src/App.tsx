import React, { Component } from 'react';
import DataStreamer, { ServerRespond } from './DataStreamer';
import Graph from './Graph';
import './App.css';

interface IState {
  data: ServerRespond[],
  showGraph: boolean,
}

class App extends Component<{}, IState> {

  private streamingInterval : number;

  constructor(props: {}) {
    super(props);
    this.streamingInterval = NaN;
    this.state = {
      data: [],
      showGraph: false,
    };
  }

  renderGraph() {
    if (this.state.showGraph) {
      return (<Graph data={this.state.data}/>)
    }
  }

  getDataFromServer() {
    this.streamingInterval = window.setInterval(() =>  {
      DataStreamer.getData((serverResponds: ServerRespond[]) => {
        // Update the state by creating a new array of data that consists of
        // Previous data in the state and the new data from server
        this.setState({ 
          data: serverResponds,
          showGraph: true,
         });
      });
    }, 100); // keep getting data every 100ms (0.1s) indefinitely
  }

  stopDataFromServer() {
    window.clearInterval(this.streamingInterval);
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          Bank Merge & Co Task 3
        </header>
        <div className="App-content">
          <button className="btn btn-primary Stream-button" onClick={() => {this.getDataFromServer()}}>Start Streaming Data</button>
          <button className="btn btn-danger Stream-button"  onClick={() => {this.stopDataFromServer()}}>Stop Streaming Data</button>
          <div className="Graph">
            {this.renderGraph()}
          </div>
        </div>
      </div>
    )
  }
}

export default App;

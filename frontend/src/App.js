import React, { Component } from 'react';

class App extends Component { 
  state = {
    software: []
  };

  async componentDidMount() { 
    try { 
      const res = await fetch('http://127.0.0.1:8000/api/api/software');
      const software = await res.json();
      this.setState ({ 
        software
      });
    } catch (e) { 
      console.log(e);
    }
  }
  
  render() {
    // return (<h1>lkj</h1>)
    return (
      <div>
        {this.state.software.map(item => (
          <div key={item.id}>
            <h1>{item.software_name}</h1>
          </div>
        ))}
      </div>
    );
  }
}


export default App;

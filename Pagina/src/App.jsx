import React, { useState, useEffect } from "react";
import "./index.css";
import axios from "axios";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import ArticuloList from "./Componentes/ArticuloList";
import Articulo from "./Componentes/Articulo";

function App() {
  return (
    <Router>
      <div className="App">
        <header>
          <h1>Minecraft Wiki</h1>
        </header>

        <Switch>
          <Route path="/" exact component={ArticuloList} />
          <Route path="/articulo/:id" component={Articulo} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;

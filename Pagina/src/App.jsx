// App.js o App.jsx
import React from 'react';
import Footer from './Componentes/footer'; // Ajusta la ruta si está en una subcarpeta
import Body from './Componentes/body';
import Header from './Componentes/header';
import "./App.css"

function App() {
  return (
    <div className="App">   
      <Header></Header>
      <Body></Body> 

      <Footer />
    </div>
  );
}

export default App;

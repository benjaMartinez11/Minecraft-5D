// Body.js
import React from 'react';
import '../index.css';

function Body() {
  return (
    <main className="body">
      <section className="main-section">
        <h1>Bienvenido a Nuestra Página</h1>
        <p>Explora nuestros servicios y conoce más sobre nosotros.</p>
      </section>
      <section className="section" id="about">
        <h2>Acerca de</h2>
        <p>Somos una empresa dedicada a ofrecer los mejores servicios.</p>
      </section>
      <section className="section" id="services">
        <h2>Servicios</h2>
        <p>Ofrecemos una amplia gama de servicios para satisfacer tus necesidades.</p>
      </section>
    </main>
  );
}

export default Body;

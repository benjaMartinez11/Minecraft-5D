import React from 'react';
import { FaInstagram, FaGithub, FaWhatsapp } from 'react-icons/fa';

const Footer = () => {
    return (
        <>
            <footer className="footer">
                <p>Creado por Brian Corbalan, Adan Coronel, Benjamin Martinez y Gregorio Tinoco.</p>
                <div className="icons">
                    <a href="#"><FaInstagram /></a>
                    <a href="#"><FaGithub /></a>
                    <a href="#"><FaWhatsapp /></a>
                </div>
            </footer>
        </>
    );
};

export default Footer;

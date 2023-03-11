import React from 'react';
import './Footer.css';

const Footer = () => {
  return (
    <div className="footer-container">
      <div className="footer-column">
        <h3>About Us</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. </p>
      </div>
      <div className="footer-column">
        <h3>Contact Us</h3>
        <p>123 Main Street, New York, NY 10001</p>
        <p>Email: info@example.com</p>
        <p>Phone: (123) 456-7890</p>
      </div>
      <div className="footer-column">
        <h3>Connect with Us</h3>
        <ul>
          <li><a href="#">Facebook</a></li>
          <li><a href="#">Twitter</a></li>
          <li><a href="#">Instagram</a></li>
        </ul>
      </div>
    </div>
  );
};

export default Footer;
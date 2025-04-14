import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';

const HotelRiskChart = () => {
 
  return (
    <div style={{ marginTop: '3rem', textAlign: 'center', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '1rem' }}>
    <a
      href="https://flightpricepredictor-qwuasxxqhrbmg8tcskk29j.streamlit.app/"
      target="_blank"
      rel="noopener noreferrer"
      style={{
        padding: '0.6rem 1.4rem',
        backgroundColor: 'teal',
        color: 'white',
        borderRadius: '10px',
        textDecoration: 'none',
        fontSize: '0.95rem',
        boxShadow: '0px 4px 12px rgba(0, 128, 128, 0.3)',
        transition: 'all 0.2s ease-in-out'
      }}
    >
      Do Flight Prices Prediction Here
    </a>
  
    <a
      href="https://hoteltiwise-7hnhjvmtxnh7ep3nff4fbg.streamlit.app/"
      target="_blank"
      rel="noopener noreferrer"
      style={{
        padding: '0.6rem 1.4rem',
        backgroundColor: 'teal',
        color: 'white',
        borderRadius: '10px',
        textDecoration: 'none',
        fontSize: '0.95rem',
        boxShadow: '0px 4px 12px rgba(0, 128, 128, 0.3)',
        transition: 'all 0.2s ease-in-out'
      }}
    >
      Explore Hotel Booking Risk Prediction
    </a>
  </div>
    );
};

export default HotelRiskChart;

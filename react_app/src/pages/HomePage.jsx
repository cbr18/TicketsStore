import React, { useEffect, useState } from "react";
import axios from 'axios';
import useAuth from '../hooks/use-auth';
import Select from 'react-select';
import { Navigate } from 'react-router-dom';

const API_URL = 'http://localhost:8000';

const HomePage = () => {
  const { isAuthenticated, getUsername } = useAuth();  
  const [city, setCity] = useState({});
  const [cities, setCities] = useState([]);

  const handleSubmit = async () => {
    console.log(city);
    return <Navigate to='/places'{...city.value} />
  }

  useEffect(() => {
  const fetchCities = async () => {
    try {
      if (cities.length === 0) {
        const response = await axios.get(`${API_URL}/cities/`);
        setCities(response.data);
      }
    } catch (error) {
      console.error('Error fetching cities:', error);
    }
  };

  fetchCities();
}, [cities.length]);

  return (
    <div>

      {isAuthenticated && <h1>Hello, {getUsername()}</h1>}

      <Select
        options={cities}
        onChange={handleSubmit()}
        
        placeholder="Выберите город"
        isSearchable
        value={city}
      />
      
    </div>
  );
};

export default HomePage;
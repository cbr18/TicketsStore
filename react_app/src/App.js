import React from 'react';
import { Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage'; 
import EventsPage from './pages/EventPage';
import AddPlacePage from './pages/AddPlacePage';
import PlacesPage from './pages/PlacesPage';
import { BrowserRouter } from 'react-router-dom';
import Navbar from './components/Navbar';

function App() {
  return (
    <div>
    <BrowserRouter>
    <Navbar/>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/events" element={ <EventsPage /> } />
        <Route path='addPlace' element={<AddPlacePage/>}/> 
          <Route path='/:city'element = {<PlacesPage />}/>
      </Routes>
      </BrowserRouter>
      </div>
  );
}

export default App
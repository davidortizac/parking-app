import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Dashboard from './pages/Dashboard';
import Login from './pages/Login';
import Register from './pages/Register';
import Reserva from './pages/Reserva';
import Vehiculos from './pages/Vehiculos';
import Sanciones from './pages/Sanciones';
import Rotacion from './pages/Rotacion';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/reserva" element={<Reserva />} />
        <Route path="/vehiculos" element={<Vehiculos />} />
        <Route path="/sanciones" element={<Sanciones />} />
        <Route path="/rotacion" element={<Rotacion />} />
      </Routes>
    </Router>
  );
}

export default App;

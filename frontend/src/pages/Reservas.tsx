import React, { useState, useEffect } from "react";
import axios from "axios";

const Reservas = () => {
  const [vehiculos, setVehiculos] = useState([]);
  const [vehiculoId, setVehiculoId] = useState("");
  const [fecha, setFecha] = useState("");
  const [franja, setFranja] = useState("manana");
  const [mensaje, setMensaje] = useState("");

  useEffect(() => {
    // Obtener vehículos del usuario (usuario_id simulado)
    axios.get(`/vehiculos?usuario_id=1`).then((res) => setVehiculos(res.data));
  }, []);

  const handleReserva = async () => {
    try {
      await axios.post("/reservas", {
        usuario_id: 1, // ID simulado, debe venir del contexto de autenticación
        vehiculo_id: parseInt(vehiculoId),
        fecha,
        franja,
        tipo: vehiculos.find(v => v.id === parseInt(vehiculoId))?.tipo
      });
      setMensaje("✅ Reserva exitosa");
    } catch (err: any) {
      setMensaje(`❌ ${err.response?.data?.detail || "Error al reservar"}`);
    }
  };

  return (
    <div className="p-4 max-w-xl mx-auto">
      <h1 className="text-xl font-bold mb-4">Reservar Parqueadero</h1>

      <label className="block mb-2">Vehículo:</label>
      <select
        className="w-full mb-4 p-2 border rounded"
        value={vehiculoId}
        onChange={(e) => setVehiculoId(e.target.value)}
      >
        <option value="">Seleccione...</option>
        {vehiculos.map((v: any) => (
          <option key={v.id} value={v.id}>
            {v.tipo.toUpperCase()} - {v.placa}
          </option>
        ))}
      </select>

      <label className="block mb-2">Fecha:</label>
      <input
        type="date"
        className="w-full mb-4 p-2 border rounded"
        value={fecha}
        onChange={(e) => setFecha(e.target.value)}
      />

      <label className="block mb-2">Franja horaria:</label>
      <select
        className="w-full mb-4 p-2 border rounded"
        value={franja}
        onChange={(e) => setFranja(e.target.value)}
      >
        <option value="manana">Mañana (8am - 12m)</option>
        <option value="tarde">Tarde (12m - 6pm)</option>
        <option value="dia_completo">Todo el día</option>
      </select>

      <button
        className="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700"
        onClick={handleReserva}
      >
        Reservar
      </button>

      {mensaje && <p className="mt-4 font-semibold">{mensaje}</p>}
    </div>
  );
};

export default Reservas;

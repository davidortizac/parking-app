import React, { useEffect, useState } from "react";
import axios from "axios";

const Dashboard = () => {
  const [disponibilidad, setDisponibilidad] = useState<any[]>([]);
  const [fecha, setFecha] = useState(() => new Date().toISOString().split("T")[0]);

  useEffect(() => {
    if (fecha) {
      axios.get(`/dashboard?fecha=${fecha}`).then((res) => setDisponibilidad(res.data));
    }
  }, [fecha]);

  return (
    <div className="p-4 max-w-3xl mx-auto">
      <h1 className="text-xl font-bold mb-4">Dashboard de Parqueaderos</h1>

      <label className="block mb-2">Fecha:</label>
      <input
        type="date"
        className="mb-4 p-2 border rounded"
        value={fecha}
        onChange={(e) => setFecha(e.target.value)}
      />

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {disponibilidad.map((cupo: any, index: number) => (
          <div
            key={index}
            className="border rounded p-4 shadow hover:shadow-md transition"
          >
            <h2 className="text-lg font-semibold mb-2">
              {cupo.tipo.toUpperCase()} - {cupo.franja.toUpperCase()}
            </h2>
            <p>
              <strong>Disponibles:</strong> {cupo.disponibles - cupo.ocupados}
            </p>
            <p>
              <strong>Ocupados:</strong> {cupo.ocupados}
            </p>
            <p>
              <strong>Usuarios:</strong> {cupo.usuarios.join(", ")}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Dashboard;

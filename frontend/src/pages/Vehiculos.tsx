import React, { useState, useEffect } from "react";
import axios from "axios";

const Vehiculos = () => {
  const [usuarios, setUsuarios] = useState([]);
  const [vehiculo, setVehiculo] = useState({
    usuario_id: "",
    tipo: "automovil",
    placa: ""
  });
  const [mensaje, setMensaje] = useState("");

  useEffect(() => {
    axios.get("/usuarios").then((res) => setUsuarios(res.data));
  }, []);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setVehiculo({ ...vehiculo, [e.target.name]: e.target.value });
  };

  const handleSubmit = async () => {
    try {
      await axios.post("/vehiculos", {
        ...vehiculo,
        usuario_id: parseInt(vehiculo.usuario_id)
      });
      setMensaje("✅ Vehículo registrado correctamente");
    } catch (err: any) {
      setMensaje(`❌ ${err.response?.data?.detail || "Error al registrar vehículo"}`);
    }
  };

  return (
    <div className="p-4 max-w-xl mx-auto">
      <h1 className="text-xl font-bold mb-4">Registro de Vehículo</h1>

      <label className="block mb-1">Usuario:</label>
      <select
        name="usuario_id"
        value={vehiculo.usuario_id}
        onChange={handleChange}
        className="w-full p-2 mb-4 border rounded"
      >
        <option value="">Seleccione un usuario...</option>
        {usuarios.map((u: any) => (
          <option key={u.id} value={u.id}>
            {u.nombre} {u.apellido} ({u.correo})
          </option>
        ))}
      </select>

      <label className="block mb-1">Tipo de Vehículo:</label>
      <select
        name="tipo"
        value={vehiculo.tipo}
        onChange={handleChange}
        className="w-full p-2 mb-4 border rounded"
      >
        <option value="automovil">Automóvil</option>
        <option value="motocicleta">Motocicleta</option>
      </select>

      <label className="block mb-1">Placa:</label>
      <input
        type="text"
        name="placa"
        value={vehiculo.placa}
        onChange={handleChange}
        className="w-full p-2 mb-4 border rounded"
      />

      <button
        onClick={handleSubmit}
        className="bg-purple-600 text-white py-2 px-4 rounded hover:bg-purple-700"
      >
        Registrar
      </button>

      {mensaje && <p className="mt-4 font-semibold">{mensaje}</p>}
    </div>
  );
};

export default Vehiculos;

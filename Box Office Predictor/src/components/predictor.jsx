import React, { useState } from 'react';
import axios from 'axios';
import './predictor.css'; 

export default function Predictor() {
  const [title, setTitle] = useState('');
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!title.trim()) return;

    setLoading(true);
    setError('');
    setPrediction(null);

    try {
      const response = await axios.post('http://localhost:5000/predict', { title });
      setPrediction(response.data.predicted_revenue);
    } catch (err) {
      setError(err.response?.data?.error || 'Error fetching prediction');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <div className="card">
        <h2 className="title">Box Office Revenue Predictor</h2>
        <form onSubmit={handleSubmit} className="form">
          <input
            type="text"
            placeholder="Enter movie title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            className="input"
            disabled={loading}
          />
          <button type="submit" disabled={loading} className="button">
            {loading ? 'Predicting...' : 'Predict Revenue'}
          </button>
        </form>

        {prediction !== null && (
          <div className="prediction">
            Predicted Revenue: ${prediction.toLocaleString(undefined, { maximumFractionDigits: 0 })}
          </div>
        )}

        {error && (
          <div className="error">
            {error}
          </div>
        )}
      </div>
    </div>
  );
}
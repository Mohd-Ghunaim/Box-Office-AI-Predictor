import React, { useState } from 'react';
import axios from 'axios';

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
    <div style={{ maxWidth: 500, margin: '2rem auto', fontFamily: 'Arial, sans-serif' }}>
      <h2>Box Office Revenue Predictor</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter movie title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          style={{ width: '100%', padding: '0.5rem', fontSize: '1rem' }}
          disabled={loading}
        />
        <button type="submit" style={{ marginTop: 10, padding: '0.5rem 1rem' }} disabled={loading}>
          {loading ? 'Predicting...' : 'Predict Revenue'}
        </button>
      </form>

      {prediction !== null && (
        <div style={{ marginTop: 20, fontWeight: 'bold' }}>
          Predicted Revenue: ${prediction.toLocaleString(undefined, { maximumFractionDigits: 0 })}
        </div>
      )}

      {error && <div style={{ marginTop: 20, color: 'red' }}>{error}</div>}
    </div>
  );
}

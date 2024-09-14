import React, { useState } from 'react';
import HasteForm from './HasteForm';
import './App.css';

const App = () => {
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleFormSubmit = async (formData) => {
    console.log('Form Data:', formData); // 调试信息
    try {
      const response = await fetch('http://localhost:5000/calculate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      const data = await response.json();
      console.log('Response Data:', data); // 调试信息
      if (response.ok) {
        setResult(data);
        setError(null);
      } else {
        setError(data.error);
        setResult(null);
      }
    } catch (err) {
      console.error('Request Error:', err); // 调试信息
      setError('请求失败，请稍后再试。');
      setResult(null);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1 className="App-title">奶妈加速小助手</h1>
      </header>
      <div className="App-content">
        <div className="App-form">
          <HasteForm onSubmit={handleFormSubmit} />
        </div>
        {error && <div className="App-error">{error}</div>}
        {result && (
          <div className="App-result">
            <h2>结果</h2>
            <p>总加速等级: {result.total_haste}</p>
            <p>溢出值: {result.overflow}</p>
            <p>选择的品阶: {result.rank}</p>
            <p>选择的武器类型: {result.weapon_type}</p>
            <h3>最优配装（套装鞋子无根骨孔）:</h3>
            <ul>
              {result.selected_equipment.map((equip, index) => (
                <li key={index}>{equip[0]}: {equip[1]}</li>
              ))}
            </ul>
            <h3>附魔选择:</h3>
            <ul>
              {result.selected_enchantments.map((enchant, index) => (
                <li key={index}>{enchant[0]}: {enchant[1]}</li>
              ))}
            </ul>
            <h3>注：由于暗器附魔存在根骨附魔，所以暂不考虑使用暗器加速附魔。</h3>
          </div>
        )}
      </div>
    </div>
  );
};

export default App;

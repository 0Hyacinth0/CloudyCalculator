import React, { useState } from 'react';

const HasteForm = ({ onSubmit }) => {
  const [threshold, setThreshold] = useState(46160);
  const [rank, setRank] = useState('普通');
  const [weaponType, setWeaponType] = useState('无加速武器');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (threshold <= 0) {
      alert("加速阈值必须大于0");
      return;
    }
    onSubmit({ threshold, rank, weaponType });
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>加速阈值:</label>
        <input
          type="number"
          value={threshold}
          onChange={(e) => setThreshold(e.target.value)}
        />
      </div>
      <div>
        <label>品阶:</label>
        <select value={rank} onChange={(e) => setRank(e.target.value)}>
          <option value="普通">普通</option>
          <option value="英雄">英雄</option>
        </select>
      </div>
      <div>
        <label>武器类型:</label>
        <select value={weaponType} onChange={(e) => setWeaponType(e.target.value)}>
          <option value="加速武器">加速武器</option>
          <option value="橙武">橙武</option>
          <option value="无加速武器">无加速武器</option>
        </select>
      </div>
      <button type="submit">计算</button>
    </form>
  );
};

export default HasteForm;

import React from 'react';

function Etran({ etran }) {
  const { etuid, quantity } = etran;
  return (
    <div className="Etran">
      <div>Etuid: {etuid}</div>
      <div>Quantity: {quantity}</div>
    </div>
  )
}

export default Etran;
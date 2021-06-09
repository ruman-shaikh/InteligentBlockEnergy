import React from 'react';

function Etran({ etran }) {
  const { input, output } = etran;
  const etuid = Object.keys(output);

  return (
    <div className="Etran">
      <div>From: {input.address}</div>
      {
        etuid.map(etuid => (
          <div key={etuid}>
            To: {etuid} | Sent: {output[etuid]}
          </div>
        ))
      }
    </div>
  )
}

export default Etran;

function Dashboard({ problems }) {

  const total = problems.length;

  const easy = problems.filter(
    p => p.difficulty === "Easy"
  ).length;

  const medium = problems.filter(
    p => p.difficulty === "Medium"
  ).length;

  const hard = problems.filter(
    p => p.difficulty === "Hard"
  ).length;

  return (
    <div className="dashboard">

  <div className="card">
    <h3>Total</h3>
    <p>{total}</p>
  </div>

  <div className="card">
    <h3>Easy</h3>
    <p>{easy}</p>
  </div>

  <div className="card">
    <h3>Medium</h3>
    <p>{medium}</p>
  </div>

  <div className="card">
    <h3>Hard</h3>
    <p>{hard}</p>
  </div>

</div>
  );
}

export default Dashboard;
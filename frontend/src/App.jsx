import { useEffect, useState } from "react";
import Header from "./components/Header";
import Dashboard from "./components/Dashboard";
import "./App.css";

function App() {

  const [problems, setProblems] = useState([]);
  const [search, setSearch] = useState("");

  const [name, setName] = useState("");
  const [topic, setTopic] = useState("");
  const [difficulty, setDifficulty] = useState("");
  const [difficultyFilter, setDifficultyFilter] = useState("All");


  useEffect(() => {

    fetch("http://127.0.0.1:8000/problems")
      .then((response) => response.json())
      .then((data) => {
        setProblems(data);
      });

  }, []);

  async function addProblem() {

    const response = await fetch(
      "http://127.0.0.1:8000/problems",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          name,
          topic,
          difficulty
        })
      }
    );

    console.log(response);

    const newResponse = await fetch(
      "http://127.0.0.1:8000/problems"
    );

    const data = await newResponse.json();

    setProblems(data);

    setName("");
    setTopic("");
    setDifficulty("");
  }

  async function deleteProblem(id) {

    const response = await fetch(
      `http://127.0.0.1:8000/problems/${id}`,
      {
        method: "DELETE"
      }
    );

    const data = await response.json();

    console.log(data);

    setProblems(
      problems.filter(
        problem => problem.id !== id
      )
    );
  }

 async function updateProblem(id) {

  const response = await fetch(
    `http://127.0.0.1:8000/problems/${id}`,
    {
      method: "PUT",

      headers: {
        "Content-Type": "application/json"
      },

      body: JSON.stringify({
        topic: "Arrays",
        difficulty: "Hard"
      })
    }
  );
  5

  const data = await response.json();

  console.log(data);

  setProblems(
    problems.map((problem) =>
      problem.id === id
        ? {
            ...problem,
            topic: "Arrays",
            difficulty: "Hard"
          }
        : problem
    )
  );
}
const filteredProblems = problems.filter(
  (problem) => {

    const matchesTopic =
      problem.topic.toLowerCase().includes(
        search.toLowerCase()
      );

    const matchesDifficulty =
      difficultyFilter === "All" ||
      problem.difficulty === difficultyFilter;

    return (
      matchesTopic &&
      matchesDifficulty
    );
  }
);
async function makeEasy(id) {

  const response = await fetch(
    `http://127.0.0.1:8000/problems/${id}`,
    {
      method: "PUT",

      headers: {
        "Content-Type": "application/json"
      },

      body: JSON.stringify({
        topic: "Arrays",
        difficulty: "Easy"
      })
    }
  );

  const data = await response.json();

  console.log(data);

  setProblems(
    problems.map((problem) =>
      problem.id === id
        ? {
            ...problem,
            difficulty: "Easy"
          }
        : problem
    )
  );
}

return (
    <div className="container">

      <Header />

      <Dashboard problems={problems} />

      <h2>Add Problem</h2>

      <input
        type="text"
        placeholder="Problem Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <br /><br />

      <input
        type="text"
        placeholder="Topic"
        style={{ width: "300px", height: "40px" }}
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
      />

      <br /><br />

      <input
        type="text"
        placeholder="Difficulty"
        style={{ width: "300px" }}
        value={difficulty}
        onChange={(e) => setDifficulty(e.target.value)}
      />

      <br /><br />

      <button onClick={() => addProblem()}>
        Add Problem
      </button>
      <h2>Search Problems</h2>

<input
  type="text"
  placeholder="Search by Topic"
  value={search}
  onChange={(e) => setSearch(e.target.value)}
/>

<br /><br />
<select
  value={difficultyFilter}
  onChange={(e) =>
    setDifficultyFilter(e.target.value)
  }
>
  <option>All</option>
  <option>Easy</option>
  <option>Medium</option>
  <option>Hard</option>
</select>

      <h2>Problems</h2>

      {filteredProblems.map((problem) => (
        <div
  key={problem.id}
  className="problem-card"
>

          <p>
  {problem.name} -
  {problem.topic} -
  <span className={problem.difficulty}>
    {problem.difficulty}
  </span>
</p>

          <button
            onClick={() => deleteProblem(problem.id)}
          >
            Delete
          </button>

          <button
            onClick={() => updateProblem(problem.id)}
          >
            Make Hard
          </button>
          <button
  onClick={() => makeEasy(problem.id)}
>
  Make Easy
</button>

          <hr />

        </div>
      ))}
 

    </div>
  );
}

export default App;

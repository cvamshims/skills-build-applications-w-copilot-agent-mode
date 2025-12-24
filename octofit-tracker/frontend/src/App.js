
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';


function App() {
  return (
    <div className="App bg-light min-vh-100">
      {/* Bootstrap Navigation */}
      <nav className="navbar navbar-expand-lg navbar-dark">
        <div className="container-fluid">
          <a className="navbar-brand d-flex align-items-center" href="#">
            <img src={process.env.PUBLIC_URL + '/octofitapp-small.svg'} alt="Octofit Logo" style={{height: '40px', marginRight: '12px'}} />
            Octofit Tracker
          </a>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav ms-auto">
              <li className="nav-item"><a className="nav-link active" href="#">Home</a></li>
              <li className="nav-item"><a className="nav-link" href="#">Activities</a></li>
              <li className="nav-item"><a className="nav-link" href="#">Teams</a></li>
              <li className="nav-item"><a className="nav-link" href="#">Leaderboard</a></li>
              <li className="nav-item"><a className="nav-link" href="#">Workouts</a></li>
            </ul>
          </div>
        </div>
      </nav>

      <div className="container py-5">
        <div className="row justify-content-center">
          <div className="col-md-8">
            <div className="card shadow">
              <div className="card-body text-center">
                <img src={logo} className="App-logo mb-3" alt="logo" />
                <h1 className="card-title display-5 mb-3">Welcome to Octofit Tracker</h1>
                <p className="card-text lead mb-4">Track your fitness activities, join teams, compete on the leaderboard, and get personalized workout suggestions!</p>
                <a className="btn btn-primary btn-lg" href="#">Get Started</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;

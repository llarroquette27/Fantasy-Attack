import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'
import Menu from './components/Menu.jsx';

// Router imports
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Home from './pages/Home.jsx';
import Teams from './pages/Teams.jsx';
import Positions from './pages/Positions.jsx';
import Search from './pages/Search.jsx';


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Router>
      <Menu />
          <Routes>
            <Route path='/' element={<Home />}/>
            <Route path='/teams' element={<Teams />}/>
            <Route path='/pos' element={<Positions />}/>
            <Route path='/search' element={<Search />}/>
            <Route path='*' element={<h1>Not Found</h1>} />
          </Routes>
        </Router>

  </React.StrictMode>,
)

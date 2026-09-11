import zipfile

files = {
    "package.json": '''{
  "name": "trekbazaar-complete-ui",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.20.0",
    "react-scripts": "5.0.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "browserslist": {
    "production": [">0.2%", "not dead", "not op_mini all"],
    "development": ["last 1 chrome version", "last 1 firefox version", "last 1 safari version"]
  }
}''',
    "public/index.html": '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>TrekBazaar - Adventure & Gear</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>''',
    "src/index.js": '''import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);''',
    "src/index.css": '''* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #f4f6f8; color: #2d3748; }
a { text-decoration: none; color: inherit; }
.container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
.btn { display: inline-block; background: #2e7d32; color: #fff; padding: 10px 20px; border-radius: 6px; font-weight: 600; cursor: pointer; border: none; }
.btn:hover { background: #1b5e20; }''',
    "src/data/treks.js": '''export const TREKS = [
  {
    id: "1",
    title: "Everest Base Camp Trek",
    location: "Nepal",
    duration: "14 Days",
    difficulty: "Challenging",
    price: "$1,450",
    image: "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=800&q=80",
    description: "Experience the pinnacle of high-altitude trekking through legendary Sherpa villages to the foot of Mount Everest."
  },
  {
    id: "2",
    title: "Inca Trail to Machu Picchu",
    location: "Peru",
    duration: "4 Days",
    difficulty: "Moderate",
    price: "$890",
    image: "https://images.unsplash.com/photo-1526392060635-9d6019884377?auto=format&fit=crop&w=800&q=80",
    description: "Hike ancient stone pathways through cloud forests ending at the sacred Sun Gate of Machu Picchu."
  },
  {
    id: "3",
    title: "Tour du Mont Blanc",
    location: "France / Italy / Switzerland",
    duration: "10 Days",
    difficulty: "Moderate to Strenuous",
    price: "$1,200",
    image: "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=800&q=80",
    description: "Circle Western Europe's highest peak across three country borders with breathtaking alpine panoramas."
  },
  {
    id: "4",
    title: "Kilimanjaro Machame Route",
    location: "Tanzania",
    duration: "7 Days",
    difficulty: "Strenuous",
    price: "$1,850",
    image: "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
    description: "Ascend Africa's highest summit through rainforests, moorlands, and volcanic desert peaks."
  }
];''',
    "src/components/Navbar.js": '''import React from 'react';
import { NavLink } from 'react-router-dom';
import './Navbar.css';

export default function Navbar() {
  return (
    <header className="navbar">
      <div className="nav-container container">
        <NavLink to="/" className="logo">🏕️ TrekBazaar</NavLink>
        <nav className="nav-links">
          <NavLink to="/" end className={({ isActive }) => isActive ? "active" : ""}>Home</NavLink>
          <NavLink to="/treks" className={({ isActive }) => isActive ? "active" : ""}>Treks</NavLink>
          <NavLink to="/about" className={({ isActive }) => isActive ? "active" : ""}>About</NavLink>
          <NavLink to="/contact" className={({ isActive }) => isActive ? "active" : ""}>Contact</NavLink>
        </nav>
      </div>
    </header>
  );
}''',
    "src/components/Navbar.css": '''.navbar { background: #1b4332; padding: 15px 0; color: white; position: sticky; top: 0; z-index: 100; }
.nav-container { display: flex; justify-content: space-between; align-items: center; }
.logo { font-size: 1.5rem; font-weight: bold; color: #52b788; }
.nav-links { display: flex; gap: 20px; }
.nav-links a { color: white; font-weight: 500; transition: color 0.2s; }
.nav-links a.active, .nav-links a:hover { color: #52b788; }''',
    "src/components/Footer.js": '''import React from 'react';

export default function Footer() {
  return (
    <footer style={{ background: '#081c15', color: '#b7e4c7', padding: '30px 0', marginTop: '50px', textAlign: 'center' }}>
      <div className="container">
        <p>&copy; {new Date().getFullYear()} TrekBazaar. All rights reserved.</p>
        <p style={{ fontSize: '0.85rem', marginTop: '8px', color: '#74c69d' }}>Connecting adventurers to legendary trails worldwide.</p>
      </div>
    </footer>
  );
}''',
    "src/pages/Home.js": '''import React from 'react';
import { Link } from 'react-router-dom';
import { TREKS } from '../data/treks';
import './Home.css';

export default function Home() {
  return (
    <div className="home-page">
      <section className="hero">
        <div className="hero-content">
          <h1>Discover Your Next Mountain Adventure</h1>
          <p>Curated trekking itineraries, expert trail guides, and premium gear.</p>
          <Link to="/treks" className="btn hero-btn">Explore All Treks</Link>
        </div>
      </section>

      <section className="featured container">
        <h2>Featured Treks</h2>
        <div className="trek-grid">
          {TREKS.map((trek) => (
            <div key={trek.id} className="trek-card">
              <img src={trek.image} alt={trek.title} />
              <div className="trek-info">
                <span className="badge">{trek.difficulty}</span>
                <h3>{trek.title}</h3>
                <p className="meta">📍 {trek.location} • ⏳ {trek.duration}</p>
                <div className="card-footer">
                  <span className="price">{trek.price}</span>
                  <Link to={`/treks/${trek.id}`} className="btn">View Details</Link>
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}''',
    "src/pages/Home.css": '''.hero { background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1600&q=80') center/cover; height: 380px; display: flex; align-items: center; justify-content: center; text-align: center; color: white; margin-bottom: 40px; }
.hero-content h1 { font-size: 2.5rem; margin-bottom: 12px; }
.hero-content p { font-size: 1.2rem; margin-bottom: 20px; color: #e0e0e0; }
.hero-btn { font-size: 1.1rem; padding: 12px 28px; }
.featured h2 { margin-bottom: 24px; color: #1b4332; }
.trek-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; }
.trek-card { background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.08); transition: transform 0.2s; }
.trek-card:hover { transform: translateY(-4px); }
.trek-card img { width: 100%; height: 200px; object-fit: cover; }
.trek-info { padding: 16px; }
.badge { background: #d8f3dc; color: #1b4332; font-size: 0.75rem; padding: 4px 8px; border-radius: 4px; font-weight: bold; }
.trek-info h3 { margin: 8px 0; font-size: 1.2rem; }
.meta { font-size: 0.9rem; color: #666; margin-bottom: 12px; }
.card-footer { display: flex; justify-content: space-between; align-items: center; margin-top: 12px; }
.price { font-size: 1.25rem; font-weight: bold; color: #2e7d32; }''',
    "src/pages/TrekList.js": '''import React from 'react';
import { Link } from 'react-router-dom';
import { TREKS } from '../data/treks';

export default function TrekList() {
  return (
    <div className="container" style={{ padding: '40px 20px' }}>
      <h1 style={{ color: '#1b4332', marginBottom: '10px' }}>All Trekking Expeditions</h1>
      <p style={{ color: '#666', marginBottom: '30px' }}>Select a trail to view full itinerary and booking requirements.</p>
      
      <div className="trek-grid">
        {TREKS.map((trek) => (
          <div key={trek.id} className="trek-card">
            <img src={trek.image} alt={trek.title} />
            <div className="trek-info">
              <span className="badge">{trek.difficulty}</span>
              <h3>{trek.title}</h3>
              <p className="meta">📍 {trek.location} • ⏳ {trek.duration}</p>
              <p style={{ fontSize: '0.9rem', color: '#555', marginBottom: '15px' }}>{trek.description}</p>
              <div className="card-footer">
                <span className="price">{trek.price}</span>
                <Link to={`/treks/${trek.id}`} className="btn">Explore Route</Link>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}''',
    "src/pages/TrekDetails.js": '''import React from 'react';
import { useParams, Link } from 'react-router-dom';
import { TREKS } from '../data/treks';

export default function TrekDetails() {
  const { id } = useParams();
  const trek = TREKS.find((t) => t.id === id);

  if (!trek) {
    return (
      <div className="container" style={{ padding: '60px 20px', textAlign: 'center' }}>
        <h2>Trek Not Found</h2>
        <p style={{ margin: '15px 0' }}>The specified trek route could not be located.</p>
        <Link to="/treks" className="btn">Back to All Treks</Link>
      </div>
    );
  }

  return (
    <div className="container" style={{ padding: '40px 20px' }}>
      <Link to="/treks" style={{ color: '#2e7d32', fontWeight: 'bold' }}>← Back to All Treks</Link>
      <div style={{ marginTop: '20px', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '30px', background: '#fff', padding: '30px', borderRadius: '8px', boxShadow: '0 4px 12px rgba(0,0,0,0.06)' }}>
        <img src={trek.image} alt={trek.title} style={{ width: '100%', borderRadius: '8px', maxHeight: '400px', objectFit: 'cover' }} />
        <div>
          <span className="badge">{trek.difficulty}</span>
          <h1 style={{ color: '#1b4332', margin: '10px 0' }}>{trek.title}</h1>
          <p style={{ fontSize: '1.1rem', color: '#666', marginBottom: '15px' }}>📍 {trek.location} | ⏳ {trek.duration}</p>
          <p style={{ lineHeight: '1.6', marginBottom: '20px' }}>{trek.description}</p>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#2e7d32', marginBottom: '20px' }}>Price: {trek.price}</div>
          <button className="btn" style={{ padding: '12px 30px', fontSize: '1rem' }} onClick={() => alert(`Booking initiated for ${trek.title}!`)}>Book Expedition Now</button>
        </div>
      </div>
    </div>
  );
}''',
    "src/pages/About.js": '''import React from 'react';

export default function About() {
  return (
    <div className="container" style={{ padding: '40px 20px' }}>
      <h1 style={{ color: '#1b4332', marginBottom: '15px' }}>About TrekBazaar</h1>
      <p style={{ fontSize: '1.1rem', lineHeight: '1.7', color: '#444', marginBottom: '25px' }}>
        TrekBazaar connects outdoor enthusiasts with verified trekking guides, high-quality gear rentals, and detailed trail maps across the world.
      </p>
      <img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80" alt="TrekBazaar Expedition" style={{ width: '100%', maxHeight: '350px', objectFit: 'cover', borderRadius: '8px' }} />
    </div>
  );
}''',
    "src/pages/Contact.js": '''import React, { useState } from 'react';

export default function Contact() {
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmitted(true);
  };

  return (
    <div className="container" style={{ padding: '40px 20px', maxWidth: '600px' }}>
      <h1 style={{ color: '#1b4332', marginBottom: '15px' }}>Contact TrekBazaar</h1>
      {submitted ? (
        <div style={{ background: '#d8f3dc', color: '#1b4332', padding: '20px', borderRadius: '6px', textAlign: 'center' }}>
          Thank you! Your inquiry has been submitted successfully.
        </div>
      ) : (
        <form onSubmit={handleSubmit} style={{ background: 'white', padding: '30px', borderRadius: '8px', boxShadow: '0 4px 12px rgba(0,0,0,0.06)' }}>
          <div style={{ marginBottom: '15px' }}>
            <label style={{ display: 'block', marginBottom: '5px', fontWeight: '600' }}>Name</label>
            <input type="text" required style={{ width: '100%', padding: '10px', borderRadius: '4px', border: '1px solid #ccc' }} />
          </div>
          <div style={{ marginBottom: '15px' }}>
            <label style={{ display: 'block', marginBottom: '5px', fontWeight: '600' }}>Email</label>
            <input type="email" required style={{ width: '100%', padding: '10px', borderRadius: '4px', border: '1px solid #ccc' }} />
          </div>
          <div style={{ marginBottom: '20px' }}>
            <label style={{ display: 'block', marginBottom: '5px', fontWeight: '600' }}>Message</label>
            <textarea required rows="4" style={{ width: '100%', padding: '10px', borderRadius: '4px', border: '1px solid #ccc' }}></textarea>
          </div>
          <button type="submit" className="btn" style={{ width: '100%' }}>Send Message</button>
        </form>
      )}
    </div>
  );
}''',
    "src/pages/NotFound.js": '''import React from 'react';
import { Link } from 'react-router-dom';

export default function NotFound() {
  return (
    <div className="container" style={{ padding: '60px 20px', textAlign: 'center' }}>
      <h1>404 - Page Not Found</h1>
      <p style={{ margin: '15px 0' }}>The requested page does not exist.</p>
      <Link to="/" className="btn">Return Home</Link>
    </div>
  );
}''',
    "src/App.js": '''import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Home from './pages/Home';
import TrekList from './pages/TrekList';
import TrekDetails from './pages/TrekDetails';
import About from './pages/About';
import Contact from './pages/Contact';
import NotFound from './pages/NotFound';

function App() {
  return (
    <Router>
      <div style={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
        <Navbar />
        <main style={{ flex: 1 }}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/treks" element={<TrekList />} />
            <Route path="/treks/:id" element={<TrekDetails />} />
            <Route path="/about" element={<About />} />
            <Route path="/contact" element={<Contact />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;'''
}

zip_name = "TrekBazaar-Complete.zip"
with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as z:
    for path, content in files.items():
        z.writestr(f"TrekBazaar-Complete/{path}", content)

print(f"Zip archive '{zip_name}' created successfully!")
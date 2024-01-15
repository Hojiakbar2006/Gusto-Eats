import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Home, Menu } from "./pages";
import { Footer, Navbar } from "./components";

const App = () => {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/menu" element={<Menu />} />
      </Routes>
      <Footer />
    </Router>
  );
};

export default App;

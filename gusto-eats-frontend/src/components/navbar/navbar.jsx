import { Button, Chip } from "@mui/material";
import { LocationOn, Person } from "@mui/icons-material";
import "./navbar.css";
import React from "react";
import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav>
      <Link to="/">
        <img width="200px" src="./brand-logo.svg" alt="" />
      </Link>
      <div className="list-items">
        <Link to="/menu">Menu</Link>
        <Chip
          sx={{ borderRadius: "5px", height: "40px" }}
          icon={<LocationOn />}
          label="Your location"
        />
        <Button
          sx={{ height: "40px", bgcolor: "#0b5dd6" }}
          startIcon={<Person />}
          disableElevation
          variant="contained"
        >
          Sign in
        </Button>
      </div>
    </nav>
  );
}

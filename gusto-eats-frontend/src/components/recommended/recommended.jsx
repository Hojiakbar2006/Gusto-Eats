import React from "react";
import "./recommended.css";
import { Link } from "react-router-dom";
import { Button, Rating } from "@mui/material";
import AddToCart from "../add-to-card/add-to-cart";

export default function Recommended() {
  const data = [
    {
      name: "Maxi BOX Taniqli",
      description:
        "Original lavash, kartoshka fri, 0,4 l coca cola, tanlash uchun sous",
      price: "40000",
      img: "https://maxway.uz/_next/image?url=https%3A%2F%2Fcdn.delever.uz%2Fdelever%2F05323470-5019-497a-b82c-62028a52acae&w=3840&q=75",
    },
    {
      name: "Maxi BOX Taniqli",
      description:
        "Original lavash, kartoshka fri, 0,4 l coca cola, tanlash uchun sous",
      price: "40000",
      img: "https://maxway.uz/_next/image?url=https%3A%2F%2Fcdn.delever.uz%2Fdelever%2F05323470-5019-497a-b82c-62028a52acae&w=3840&q=75",
    },
    {
      name: "Maxi BOX Taniqli",
      description:
        "Original lavash, kartoshka fri, 0,4 l coca cola, tanlash uchun sous",
      price: "40000",
      img: "https://maxway.uz/_next/image?url=https%3A%2F%2Fcdn.delever.uz%2Fdelever%2F05323470-5019-497a-b82c-62028a52acae&w=3840&q=75",
    },
    {
      name: "Maxi BOX Taniqli",
      description:
        "Original lavash, kartoshka fri, 0,4 l coca cola, tanlash uchun sous",
      price: "40000",
      img: "https://maxway.uz/_next/image?url=https%3A%2F%2Fcdn.delever.uz%2Fdelever%2F05323470-5019-497a-b82c-62028a52acae&w=3840&q=75",
    },
    {
      name: "Maxi BOX Taniqli",
      description:
        "Original lavash, kartoshka fri, 0,4 l coca cola, tanlash uchun sous",
      price: "40000",
      img: "https://maxway.uz/_next/image?url=https%3A%2F%2Fcdn.delever.uz%2Fdelever%2F05323470-5019-497a-b82c-62028a52acae&w=3840&q=75",
    },
    {
      name: "Maxi BOX Taniqli",
      description:
        "Original lavash, kartoshka fri, 0,4 l coca cola, tanlash uchun sous",
      price: "40000",
      img: "https://maxway.uz/_next/image?url=https%3A%2F%2Fcdn.delever.uz%2Fdelever%2F05323470-5019-497a-b82c-62028a52acae&w=3840&q=75",
    },
    {
      name: "Maxi BOX Taniqli",
      description:
        "Original lavash, kartoshka fri, 0,4 l coca cola, tanlash uchun sous",
      price: "40000",
      img: "https://maxway.uz/_next/image?url=https%3A%2F%2Fcdn.delever.uz%2Fdelever%2F05323470-5019-497a-b82c-62028a52acae&w=3840&q=75",
    },
    {
      name: "Maxi BOX Taniqli",
      description:
        "Original lavash, kartoshka fri, 0,4 l coca cola, tanlash uchun sous",
      price: "40000",
      img: "https://maxway.uz/_next/image?url=https%3A%2F%2Fcdn.delever.uz%2Fdelever%2F05323470-5019-497a-b82c-62028a52acae&w=3840&q=75",
    },
  ];
  return (
    <>
      <div className="container">
        <div className="comp-container">
          <div className="recommended">
            <div className="title">
              <h1>Recommended foods</h1>
              <p>We recommend you the most popular and discounted foods </p>
            </div>
            <div className="food-container">
              {data.map((item) => {
                return (
                  <div className="box">
                    <figure>
                      <img src={item.img} alt="" />
                      <div className="chip">15%</div>
                    </figure>
                    <div className="box-items">
                      <h2>{item.name}</h2>
                      <p>{item.description}</p>
                      <Rating name="read-only" value={3} readOnly />

                      <div className="group">
                        <p>{item.price}</p>
                        <Button
                          sx={{ height: "40px", bgcolor: "#0b5dd6" }}
                          disableElevation
                          variant="contained"
                        >
                          Add to cart
                        </Button>
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
            <Link to="/menu">
              <Button variant="outlined">for more {">>"}</Button>
            </Link>
          </div>
        </div>
      </div>
      <AddToCart />
    </>
  );
}

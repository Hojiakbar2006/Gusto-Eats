import React from "react";
import "./profile.css";
import { useGetProfileQuery } from "../../redux/services/authApi";
import { LinearProgress } from "@mui/material";
import { UpdateProfileForm } from "../../components";
import { useGetOrdersQuery } from "../../redux/services/orderApi";

export default function Profile() {
  const { data: profile, isLoading: profileLoad } = useGetProfileQuery();
  const { data: order, isLoading: orderLoad } = useGetOrdersQuery();

  if (profileLoad || orderLoad) {
    return (
      <div className="loading">
        <LinearProgress />
      </div>
    );
  }
  return (
    <div className="container">
      <div className="profile">
        <UpdateProfileForm data={profile} />
        <div className="comp-container">
          {order ? <h1>No order</h1> : <div></div>}
        </div>
      </div>
    </div>
  );
}

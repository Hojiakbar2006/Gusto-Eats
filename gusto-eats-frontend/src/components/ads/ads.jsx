import React from "react";
import { ads_img } from "../../utils/helper";
import { ImageListItem } from "@mui/material";

export default function Ads() {
  return (
    <div className="container">
      <div className="comp-container">
        <ImageListItem>
          <img src={`${ads_img}?w=248&fit=crop&auto=format`} loading="lazy" />
        </ImageListItem>
      </div>
    </div>
  );
}

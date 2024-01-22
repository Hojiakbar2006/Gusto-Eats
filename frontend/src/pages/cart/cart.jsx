import React, { useEffect } from "react";
import "./cart.css";
import { useSelector, useDispatch } from "react-redux";
import { DeleteForeverOutlined } from "@mui/icons-material";
import { Box, Grid, IconButton, TextField } from "@mui/material";
import AddIcon from "@mui/icons-material/Add";
import { Remove } from "@mui/icons-material";
import {
  addQty,
  getCartItems,
  removeFromCart,
  removeQty,
} from "../../redux/slice/cartSlice";
import { red } from "@mui/material/colors";
import { LoadingButton } from "@mui/lab";
import { Link, useNavigate } from "react-router-dom";
import { useFormik } from "formik";
import { useCreateOrderMutation } from "../../redux/services/orderApi";
import { useSnackbar } from "notistack";
import * as Yup from "yup";

export default function Cart() {
  const dispatch = useDispatch();
  const cart = useSelector((state) => state.cart);

  useEffect(() => {
    dispatch(getCartItems());
  }, [dispatch]);

  const [login, { isLoading }] = useCreateOrderMutation();
  const { enqueueSnackbar } = useSnackbar();
  const navigate = useNavigate();

  const LoginSchema = Yup.object().shape({
    email: Yup.string().email("Invalid email").required("Required"),
    password: Yup.string()
      .required("Required")
      .min(6, "Password should be at least 6 characters"),
  });

  const formik = useFormik({
    initialValues: {
      email: "",
      password: "",
    },
    validationSchema: LoginSchema,
    onSubmit: async (values) => {
      try {
        const res = await login(values);
        const { error, data } = res;
        if (data) {
          console.log(data);
          enqueueSnackbar("Kirish muvafaqiyatli amalga oshirildi", {
            variant: "success",
          });
          localStorage.setItem("access_token", data.access_token);
          localStorage.setItem("refresh_token", data.refresh_token);

          navigate("/profile/");
        }
        if (error) {
          if (error.status === 400) {
            enqueueSnackbar("Foydalanuvchi ma'lumotlari to'liq emas", {
              variant: "error",
            });
          }
          if (error.status === 401) {
            enqueueSnackbar("Foydalanuvchi ma'lumotlari topilmadi", {
              variant: "error",
            });
          }
        }
      } catch (error) {
        console.error("Login error:", error);
      }
    },
  });

  return (
    <div className="cart-container">
      <div className="comp-container">
        {cart.cartItems.length !== 0 ? (
          <>
            {cart.cartItems.map((item) => {
              const img =
                item.image && !item.image.startsWith("http")
                  ? `${process.env.REACT_APP_BASE_URL}${item.image}`
                  : item.image;
              return (
                <div className="cart-box" key={item.id}>
                  <div>
                    <figure>
                      <img width="100%" src={img} alt={item.name} />
                    </figure>
                    <h3>{item.name}</h3>
                  </div>
                  <div>
                    <IconButton onClick={() => dispatch(addQty(item))}>
                      <AddIcon />
                    </IconButton>
                    <span>{item.quantity}</span>
                    <IconButton onClick={() => dispatch(removeQty(item))}>
                      <Remove />
                    </IconButton>
                  </div>
                  <IconButton onClick={() => dispatch(removeFromCart(item))}>
                    <DeleteForeverOutlined sx={{ color: red[500] }} />
                  </IconButton>
                </div>
              );
            })}
            <h2>
              Sub total:
              {cart.total}
            </h2>
          </>
        ) : (
          <div className="message">
            <h1>No Items</h1>
          </div>
        )}
      </div>
      <div className="comp-container">
        <Box component="form" onSubmit={formik.handleSubmit} noValidate>
          <TextField
            margin="normal"
            required
            fullWidth
            id="email"
            label="Email Address"
            name="email"
            autoComplete="off"
            autoFocus
            value={formik.values.email}
            onChange={formik.handleChange}
            error={formik.touched.email && Boolean(formik.errors.email)}
            helperText={formik.touched.email && formik.errors.email}
          />
          <TextField
            margin="normal"
            required
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            autoComplete="off"
            value={formik.values.password}
            onChange={formik.handleChange}
            error={formik.touched.password && Boolean(formik.errors.password)}
            helperText={formik.touched.password && formik.errors.password}
          />
          <LoadingButton
            fullWidth
            sx={{
              height: "50px",
              fontSize: "18px",
              bgcolor: "#0b5dd6",
              marginBottom: 2,
              marginTop: 2,
            }}
            type="submit"
            variant="contained"
            loading={isLoading}
            loadingIndicator="Loading…"
          >
            Login
          </LoadingButton>
          <Grid container>
            <Grid item xs>
              <Link href="#" variant="body2">
                Forgot password?
              </Link>
            </Grid>
            <Grid item>
              <Link to="/register/" variant="body2">
                {"Don't have an account? Sign Up"}
              </Link>
            </Grid>
          </Grid>
        </Box>
      </div>
    </div>
  );
}

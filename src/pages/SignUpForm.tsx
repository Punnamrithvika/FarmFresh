import { useState, useEffect } from "react";

const SignUpForm = ({ location }: { location: string }) => {
  const [userLocation, setUserLocation] = useState("");

  useEffect(() => {
    if (location) {
      setUserLocation(location);
    }
  }, [location]);

  return (
    <form className="container mt-4">
      <div className="form-group">
        <label htmlFor="name">Name</label>
        <input type="text" className="form-control" id="name" placeholder="Enter your name" />
      </div>

      <div className="form-group">
        <label htmlFor="email">Email</label>
        <input type="email" className="form-control" id="email" placeholder="Enter your email" />
      </div>

      <div className="form-group">
        <label htmlFor="location">Location</label>
        <input type="text" className="form-control" id="location" value={userLocation} placeholder="Enter your location" readOnly />
      </div>

      <div className="form-group">
        <label htmlFor="farmLocation">Farm Location</label>
        <input type="text" className="form-control" id="farmLocation" placeholder="Enter your farm location" />
      </div>

      <div className="form-group">
        <label htmlFor="farmDescription">Farm Description</label>
        <textarea className="form-control" id="farmDescription" placeholder="Describe your farm"></textarea>
      </div>

      <div className="form-group">
        <label htmlFor="phoneNumber">Phone Number</label>
        <input type="tel" className="form-control" id="phoneNumber" placeholder="Enter your phone number" />
      </div>

      <div className="form-group">
        <label htmlFor="password">Password</label>
        <input type="password" className="form-control" id="password" placeholder="Enter your password" />
      </div>

      <button type="submit" className="btn btn-primary">Sign Up</button>
    </form>
  );
};

export default SignUpForm;
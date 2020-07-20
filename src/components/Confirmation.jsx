import React from "react";
import { Toast } from "react-bootstrap";

export function Confirmation({ toggle }) {
  return (
    <Toast onClose={() => toggle(false)}>
      <Toast.Header>
        <strong className="mr-auto"> You've selected your champion!</strong>
        <small> just now </small>
      </Toast.Header>
      <Toast.Body>The game will start soon!</Toast.Body>
    </Toast>
  );
}

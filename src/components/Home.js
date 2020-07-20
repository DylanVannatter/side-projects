import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import { Container, Row, Col } from "react-bootstrap";
import { Champions } from "./Champions";
import { Confirmation } from "./Confirmation";
import champs from "../data.json";

export function Home() {
  const [selected, setSelected] = useState(false);

  function displayConfirmation() {
    setSelected(true);

    setTimeout(() => {
      setSelected(false);
    }, 3000);
  }

  return (
    <Container>
      {selected && <Confirmation toggle={setSelected} />}
      <Row>
        {champs.map((data) => (
          <Col xs={3} className="mb-5" key={"${data.id}"}>
            <Champions data={data} setSelected={displayConfirmation} />
          </Col>
        ))}
      </Row>
    </Container>
  );
}

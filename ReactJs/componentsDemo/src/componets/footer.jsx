function Footer() {
  let footerStyles = {
    backgroundColor: "black",
    color: "white",
    padding: "10px",
    textAlign: "center",
    position: "fixed",
    bottom: "0",
    width: "100%"
  };

  return (
    <footer style={footerStyles}>
      This website belongs to &copy; Rohit 2026
    </footer>
  );
}

export default Footer;
import Layout from "./components/layout/Layout";
import Sidebar from "./components/sidebar/Sidebar";
import Home from "./pages/Home";

function App() {
  return (
    <Layout sidebar={<Sidebar />}>
      <Home />
    </Layout>
  );
}

export default App;
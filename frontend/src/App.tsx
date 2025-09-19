import { Route, Routes } from 'react-router-dom';

import ImportReviewPage from './pages/ImportReviewPage';

function App() {
  return (
    <Routes>
      <Route path="/" element={<ImportReviewPage />} />
    </Routes>
  );
}

export default App;

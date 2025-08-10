import { Toaster } from "@/components/ui/toaster";
import { Toaster as Sonner } from "@/components/ui/sonner";
import { TooltipProvider } from "@/components/ui/tooltip";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Index from "./pages/Index";
import BillNoteSheet from "./pages/BillNoteSheet";
import DeductionsTable from "./pages/DeductionsTable";
import DelayCalculator from "./pages/DelayCalculator";
import EMDRefund from "./pages/EMDRefund";
import ExcelSeEMD from "./pages/ExcelSeEMD";
import FinancialProgress from "./pages/FinancialProgress";
import SecurityRefund from "./pages/SecurityRefund";
import StampDuty from "./pages/StampDuty";
import NotFound from "./pages/NotFound";

const queryClient = new QueryClient();

const App = () => (
  <QueryClientProvider client={queryClient}>
    <TooltipProvider>
      <Toaster />
      <Sonner />
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Index />} />
          <Route path="/bill-note-sheet" element={<BillNoteSheet />} />
          <Route path="/deductions-table" element={<DeductionsTable />} />
          <Route path="/delay-calculator" element={<DelayCalculator />} />
          <Route path="/emd-refund" element={<EMDRefund />} />
          <Route path="/excel-se-emd" element={<ExcelSeEMD />} />
          <Route path="/financial-progress" element={<FinancialProgress />} />
          <Route path="/security-refund" element={<SecurityRefund />} />
          <Route path="/stamp-duty" element={<StampDuty />} />
          {/* ADD ALL CUSTOM ROUTES ABOVE THE CATCH-ALL "*" ROUTE */}
          <Route path="*" element={<NotFound />} />
        </Routes>
      </BrowserRouter>
    </TooltipProvider>
  </QueryClientProvider>
);

export default App;

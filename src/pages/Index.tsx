import craneLogo from "@/assets/crane-logo.png";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { FileText, Calculator, Percent, Clock, Shield, LineChart, FileSpreadsheet, FileCheck, ArrowRight } from "lucide-react";

// Import all tool components
import BillNoteSheet from "./BillNoteSheet";
import DeductionsTable from "./DeductionsTable";
import DelayCalculator from "./DelayCalculator";
import EMDRefund from "./EMDRefund";
import ExcelSeEMD from "./ExcelSeEMD";
import FinancialProgress from "./FinancialProgress";
import SecurityRefund from "./SecurityRefund";
import StampDuty from "./StampDuty";

const tools = [
  { 
    id: "bill-note-sheet",
    title: "Bill Note Sheet", 
    description: "Generate documents strictly as per approved templates.",
    icon: FileText,
    route: "/bill-note-sheet"
  },
  { 
    id: "deductions-table",
    title: "Deductions Table", 
    description: "Calculate standard and custom deductions.",
    icon: Percent,
    route: "/deductions-table"
  },
  { 
    id: "delay-calculator",
    title: "Delay Calculator", 
    description: "Calculate delays and penalties.",
    icon: Clock,
    route: "/delay-calculator"
  },
  { 
    id: "emd-refund",
    title: "EMD Refund", 
    description: "Process EMD refunds.",
    icon: FileCheck,
    route: "/emd-refund"
  },
  { 
    id: "excel-se-emd",
    title: "Excel to EMD", 
    description: "Convert Excel to EMD formats.",
    icon: FileSpreadsheet,
    route: "/excel-to-emd"
  },
  { 
    id: "financial-progress",
    title: "Financial Progress", 
    description: "Track financial progress.",
    icon: LineChart,
    route: "/financial-progress"
  },
  { 
    id: "security-refund",
    title: "Security Refund", 
    description: "Process security refunds.",
    icon: Shield,
    route: "/security-refund"
  },
  { 
    id: "stamp-duty",
    title: "Stamp Duty", 
    description: "Calculate stamp duties.",
    icon: FileText,
    route: "/stamp-duty"
  }
];

const Index = () => {
  return (
    <div className="min-h-screen flex flex-col bg-background">
      {/* Compact Header with Blue Background */}
      <header className="w-full border-b border-border bg-blue-600 text-white sticky top-0 z-50">
        <div className="container mx-auto px-3 py-2 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <img src={craneLogo} alt="PWD" width={28} height={28} className="rounded bg-white p-0.5" />
            <h1 className="text-lg font-semibold">PWD Tools</h1>
          </div>
          <p className="text-xs text-blue-100 hidden sm:inline">
            Initiative: Mrs. Premlata Jain, AAO, PWD Udaipur
          </p>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-1 container mx-auto px-4 py-6">
        {/* Hero Section */}
        <section className="mb-12 text-center">
          <h1 className="text-3xl md:text-4xl font-bold mb-3">PWD Tools Suite</h1>
          <p className="text-lg text-muted-foreground max-w-3xl mx-auto">
            Comprehensive set of tools for PWD workflows, designed for accuracy and efficiency in statutory documentation.
          </p>
        </section>

        {/* Tools Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          {tools.map((tool) => (
            <Card key={tool.id} className="hover:shadow-md transition-shadow">
              <CardHeader className="p-4 pb-2">
                <div className="flex items-center gap-3">
                  <div className="p-2 rounded-lg bg-blue-50 text-blue-600">
                    <tool.icon className="w-5 h-5" />
                  </div>
                  <div>
                    <h3 className="font-medium">{tool.title}</h3>
                    <p className="text-sm text-muted-foreground">{tool.description}</p>
                  </div>
                </div>
              </CardHeader>
              <CardContent className="p-4 pt-0">
                <Button className="w-full" asChild>
                  <a href={tool.route}>
                    Open {tool.title}
                  </a>
                </Button>
              </CardContent>
            </Card>
          ))}
        </div>

        {/* External Tools Section */}
        <section className="mb-12">
          <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
            <ArrowRight className="w-5 h-5 text-muted-foreground" />
            External Tools
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <FileText className="w-5 h-5" />
                  Bill Deviation
                </CardTitle>
                <CardDescription>External tool for bill deviation analysis</CardDescription>
              </CardHeader>
              <CardContent>
                <Button variant="outline" className="w-full" asChild>
                  <a href="#" target="_blank" rel="noopener noreferrer">
                    Open Bill Deviation Tool
                  </a>
                </Button>
              </CardContent>
            </Card>
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <FileText className="w-5 h-5" />
                  Tender Processing
                </CardTitle>
                <CardDescription>External tool for tender processing</CardDescription>
              </CardHeader>
              <CardContent>
                <Button variant="outline" className="w-full" asChild>
                  <a href="#" target="_blank" rel="noopener noreferrer">
                    Open Tender Processing Tool
                  </a>
                </Button>
              </CardContent>
            </Card>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="border-t border-border py-4 text-center text-sm text-muted-foreground bg-card">
        <div className="container mx-auto px-4">
          <p> 2024 PWD Tools - All Rights Reserved</p>
          <p className="text-xs mt-1">Developed for Public Works Department, Rajasthan</p>
        </div>
      </footer>
    </div>
  );
};

export default Index;

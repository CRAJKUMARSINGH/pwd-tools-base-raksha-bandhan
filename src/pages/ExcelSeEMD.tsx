import SEO from "@/components/SEO";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Link } from "react-router-dom";

const ExcelSeEMD = () => {
  return (
    <div className="container mx-auto py-10">
      <SEO title="Excel se EMD Refund — External Tool" description="Use the external Excel-based EMD refund tool." />
      <header className="mb-6">
        <h1 className="text-3xl font-bold">Excel se EMD Refund</h1>
        <p className="text-muted-foreground">External Python app embedded below.</p>
      </header>
      <Card className="elevated">
        <CardHeader>
          <CardTitle>Interactive Tool</CardTitle>
          <CardDescription>Hosted on onrender.com</CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="w-full overflow-hidden rounded-md border">
            <iframe
              src="https://marudharhr.onrender.com/"
              title="Excel se EMD Refund (onrender)"
              className="w-full h-[70vh] bg-background"
              loading="lazy"
            />
          </div>
          <div className="flex gap-3">
            <Button asChild variant="secondary"><a href="https://marudharhr.onrender.com/" target="_blank" rel="noopener noreferrer">Open full page</a></Button>
            <Button asChild><Link to="/">Back to Dashboard</Link></Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default ExcelSeEMD;

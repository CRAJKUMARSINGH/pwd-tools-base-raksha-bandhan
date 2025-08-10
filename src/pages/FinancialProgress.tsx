import SEO from "@/components/SEO";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Link } from "react-router-dom";

const FinancialProgress = () => {
  return (
    <div className="container mx-auto py-10">
      <SEO title="Financial Progress — Integrated PWD Tools" description="Monitor approvals and expenditures using the embedded tracker." />
      <header className="mb-6">
        <h1 className="text-3xl font-bold">Financial Progress Tracker</h1>
        <p className="text-muted-foreground">Live tool embedded below.</p>
      </header>
      <Card className="elevated">
        <CardHeader>
          <CardTitle>Interactive Tool</CardTitle>
          <CardDescription>Powered by pwd-tools.pages.dev</CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="w-full overflow-hidden rounded-md border">
            <iframe
              src="https://pwd-tools.pages.dev/src/components/FinancialProgressTracker.html"
              title="Financial Progress Tracker tool (PWD Tools)"
              className="w-full h-[70vh]"
              loading="lazy"
            />
          </div>
          <div className="flex gap-3">
            <Button asChild variant="secondary"><a href="https://pwd-tools.pages.dev/src/components/FinancialProgressTracker.html" target="_blank" rel="noopener noreferrer">Open full page</a></Button>
            <Button asChild><Link to="/">Back to Dashboard</Link></Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default FinancialProgress;

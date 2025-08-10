import SEO from "@/components/SEO";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Link } from "react-router-dom";

const DelayCalculator = () => {
  return (
    <main className="container mx-auto py-10">
      <SEO title="Delay Calculator — Integrated PWD Tools" description="Compute delays and penalties using the live embedded tool." />

      <header className="mb-6 rounded-2xl border p-6 ring-1 ring-[hsl(var(--magenta)/0.25)] bg-[hsl(var(--magenta)/0.05)]">
        <h1 className="text-3xl font-bold">Delay Calculator</h1>
        <p className="text-muted-foreground">Live tool embedded below.</p>
      </header>

      <section aria-labelledby="delay-calculator">
        <Card className="elevated hover-lift border-[hsl(var(--magenta)/0.25)]">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <span className="inline-block h-2.5 w-2.5 rounded-full bg-[hsl(var(--magenta))]" aria-hidden="true" />
              Interactive Tool
            </CardTitle>
            <CardDescription>Powered by pwd-tools.pages.dev</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="w-full overflow-hidden rounded-md border border-[hsl(var(--magenta)/0.25)] ring-1 ring-[hsl(var(--magenta)/0.15)]">
              <iframe
                src="https://pwd-tools.pages.dev/src/components/DelayCalculator.html"
                title="Delay Calculator tool (PWD Tools)"
                className="w-full h-[70vh] bg-background"
                loading="lazy"
              />
            </div>
            <div className="flex gap-3">
              <Button asChild variant="secondary"><a href="https://pwd-tools.pages.dev/src/components/DelayCalculator.html" target="_blank" rel="noopener noreferrer">Open full page</a></Button>
              <Button asChild><Link to="/">Back to Dashboard</Link></Button>
            </div>
          </CardContent>
        </Card>
      </section>
    </main>
  );
};

export default DelayCalculator;

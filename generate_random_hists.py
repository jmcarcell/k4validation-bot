import ROOT
import numpy as np

# Generate normally distributed random samples
# Using numpy for easier random generation
np.random.seed(42)  # For reproducibility
sample1 = np.random.normal(2.5, 1.0, 1000)  # mean=2.5, std=1.0, 1000 points
sample2 = np.random.normal(2.0, 1.2, 1000)  # mean=2.0, std=1.2, 1000 points

# Create separate ROOT files for each histogram
output_file1 = ROOT.TFile("hist1.root", "RECREATE")
hist1 = ROOT.TH1F("hist", "Normal Distribution;Value;Counts", 50, 0, 5)

# Fill the first histogram
for value in sample1:
    if 0 <= value <= 5:  # Only fill values within range
        hist1.Fill(value)

# Set colors for first histogram
hist1.SetLineColor(ROOT.kBlue)
hist1.SetFillColor(ROOT.kBlue)
hist1.SetFillStyle(3004)  # Hatched pattern

# Write and close first file
hist1.Write()
entries1 = hist1.GetEntries()
output_file1.Close()

# Create second ROOT file
output_file2 = ROOT.TFile("hist2.root", "RECREATE")
hist2 = ROOT.TH1F("hist", "Normal Distribution;Value;Counts", 50, 0, 5)

# Fill the second histogram
for value in sample2:
    if 0 <= value <= 5:  # Only fill values within range
        hist2.Fill(value)

# Set colors for second histogram
hist2.SetLineColor(ROOT.kRed)
hist2.SetFillColor(ROOT.kRed)
hist2.SetFillStyle(3005)  # Different hatched pattern

# Write and close second file
hist2.Write()
entries2 = hist2.GetEntries()
output_file2.Close()

# For plotting, we need to reopen the files
file1 = ROOT.TFile("hist1.root", "READ")
file2 = ROOT.TFile("hist2.root", "READ")
hist1_plot = file1.Get("hist")
hist2_plot = file2.Get("hist")

# Create a canvas to draw the histograms
canvas = ROOT.TCanvas("canvas", "Normal Distributions", 800, 600)

# Draw both histograms on the same canvas
hist1_plot.Draw("HIST")  # Draw first histogram
hist2_plot.Draw("HIST SAME")  # Draw second histogram on the same canvas

# Add a legend
legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
legend.AddEntry(hist1_plot, "Mean=2.5, Std=1.0", "f")
legend.AddEntry(hist2_plot, "Mean=2.0, Std=1.2", "f")
legend.Draw()

# Update the canvas to show the plot
canvas.Update()

print("Created hist1.root and hist2.root with normal distribution histograms")
print(f"Histogram 1: {entries1} entries")
print(f"Histogram 2: {entries2} entries")

# Keep the window open - wait for user input
input("Press Enter to close the plot and exit...")

# Close the read files
file1.Close()
file2.Close()
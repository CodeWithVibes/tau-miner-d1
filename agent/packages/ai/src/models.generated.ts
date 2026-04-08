import type { Model } from "./types.js";

// Miner build optimization:
// Tau validators inject the active solve model through models.json at runtime,
// so we keep the built-in catalog empty to reduce compile time and memory usage.
export const MODELS: Record<string, Record<string, Model<any>>> = {};

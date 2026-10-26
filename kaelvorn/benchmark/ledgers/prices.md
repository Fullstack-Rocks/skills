# Published model prices

As of **2026-10-26**. Every linked source below was read on **2026-10-26**. Currency is USD. Token rates are per **1,000,000 tokens**; image rates are dollars **per generated image**. The benchmark basis is public Standard API pricing, or Cursor's published token rates where available. These are usage valuations, not the project's actual subscription bills. Taxes, negotiated discounts, regional premiums, search/tool calls, and other non-token charges are excluded.

## Subscription access and benchmark basis

| Used through | Normal product billing | Benchmark valuation |
| --- | --- | --- |
| Codex CLI | ChatGPT plan usage and, where applicable, extra credits; API-key use is billed separately. | OpenAI API-equivalent prices below. Subscription limits cannot be converted directly into API dollars. [OpenAI Codex pricing](https://learn.chatgpt.com/docs/pricing), read 2026-10-26. |
| Cursor | Cursor subscription: Grok uses the included Cursor-model pool; additional usage has token rates. GPT-5.6 Sol uses prepaid credit on current plans and the Other Models pool on legacy plans. | Cursor's own published rates below. [Grok billing](https://cursor.com/docs/models/grok-4-7) and [GPT billing](https://cursor.com/docs/models/gpt-5-6-sol), read 2026-10-26. |
| Antigravity | Free access or Google AI Pro/Ultra subscription with different limits. | Gemini API-equivalent rates below; direct Gemini API calls use API billing. [Antigravity plans](https://antigravity.google/pricing), read 2026-10-26. |

## Text models

| Model / input length | Input | Cached input | Output | Source, read date |
| --- | ---: | ---: | ---: | --- |
| `gpt-6.1-sol`, up to 272K | 2.00 | 0.10 | 10.00 | [OpenAI model pricing](https://developers.openai.com/api/docs/models/gpt-6.1-sol), 2026-10-26 |
| `gpt-6.1-sol`, over 272K | 4.00 | 0.20 | 15.00 | [OpenAI model pricing](https://developers.openai.com/api/docs/models/gpt-6.1-sol), 2026-10-26 |
| `gpt-5.6-sol`, up to 272K | 4.00 | 0.40 | 20.00 | [Cursor model pricing](https://cursor.com/docs/models/gpt-5-6-sol), 2026-10-26 |
| `gpt-5.6-sol`, over 272K | 8.00 | 0.80 | 30.00 | [Cursor model pricing](https://cursor.com/docs/models/gpt-5-6-sol), 2026-10-26 |
| `grok-4.7`, up to 256K | 2.00 | 0.50 | 6.00 | [Cursor model pricing](https://cursor.com/docs/models/grok-4-7), 2026-10-26 |
| `grok-4.7`, over 256K, up to 500K context | 4.00 | 1.00 | 12.00 | [Cursor model pricing](https://cursor.com/docs/models/grok-4-7), 2026-10-26 |
| `gemini-4-argon`, all supported context lengths | 2.00 | 0.10 | 10.00 | [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing#gemini-4-argon), 2026-10-26 |

For both OpenAI models, the long-context tier applies to the **whole request**, including output, when input exceeds the threshold. GPT-6.1 Sol has a 1,050,000-token context window. [OpenAI model page](https://developers.openai.com/api/docs/models/gpt-6.1-sol), read 2026-10-26. Cursor publishes the same whole-request multipliers for GPT-5.6 Sol. [Cursor GPT page](https://cursor.com/docs/models/gpt-5-6-sol), read 2026-10-26. Grok also selects its whole-request tier by input length alone. [Cursor Grok page](https://cursor.com/docs/models/grok-4-7), read 2026-10-26.

Gemini 4 Argon has **no separate long-context price published**. Its unified input/thinking/output window is 1,048,576 tokens. [Google model specification](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon), read 2026-10-26. The current promotional Standard rates above last through **2026-11-30**; Google publishes input/cached/output rates of **4.00 / 0.20 / 20.00** starting **2026-12-01**. Caching is implicit only. [Google pricing](https://ai.google.dev/gemini-api/docs/pricing#gemini-4-argon), read 2026-10-26.

Reasoning is billed at the output rate for the OpenAI models; do not add reasoning tokens again when already included in output totals. [OpenAI reasoning documentation](https://developers.openai.com/api/docs/guides/reasoning), read 2026-10-26. Google's output rate includes thinking. [Google pricing](https://ai.google.dev/gemini-api/docs/pricing#gemini-4-argon), read 2026-10-26. Cursor publishes no separate reasoning tariff for Grok 4.7; use its billed output total and do not assume reasoning is free. [Cursor Grok pricing](https://cursor.com/docs/models/grok-4-7), read 2026-10-26.

### Cache writes and speed tiers

Cache-read prices above are not cache-write prices. OpenAI publishes GPT-6.1 Sol cache writes of **2.50** for 30 minutes and **5.00** for 12 hours; long context doubles these. [OpenAI API pricing](https://developers.openai.com/api/docs/pricing), read 2026-10-26. Cursor publishes GPT-5.6 Sol cache writes of **5.00**, or **10.00** for long context. [Cursor GPT pricing](https://cursor.com/docs/models/gpt-5-6-sol), read 2026-10-26. Apply these only to separately billed cache-write counts, using the provider's usage categories.

The JSON defaults to Standard speed. A bare model name does not establish the speed used:

| Model / alternate speed | Input | Cached input | Output | Long-context input / cached / output | Source, read date |
| --- | ---: | ---: | ---: | --- | --- |
| GPT-5.6 Sol Fast | 8.00 | 0.80 | 40.00 | 16.00 / 1.60 / 60.00 | [Cursor GPT pricing](https://cursor.com/docs/models/gpt-5-6-sol), 2026-10-26 |
| Grok 4.7 Fast | 4.00 | 1.00 | 12.00 | 6.00 / 1.50 / 18.00 | [Cursor Grok pricing](https://cursor.com/docs/models/grok-4-7), 2026-10-26 |

Cursor says Grok Fast is the default on Premium and higher and legacy Pro/Pro+/Ultra; verify session settings before using Standard. GPT Fast cache writes are **10.00**, or **20.00** for long context. [Cursor Grok page](https://cursor.com/docs/models/grok-4-7) and [GPT page](https://cursor.com/docs/models/gpt-5-6-sol), read 2026-10-26. GPT-6.1 Sol API Fast is 2× Standard, Ultrafast 6×, and Batch/Flex 0.5×. [OpenAI model page](https://developers.openai.com/api/docs/models/gpt-6.1-sol), read 2026-10-26.

## Codex built-in image generation

OpenAI explicitly identifies the built-in model as **`gpt-image-2`**. It draws from general Codex subscription usage. [OpenAI image-generation product documentation](https://learn.chatgpt.com/docs/image-generation), read 2026-10-26. This identifies the current product model; saved pixel dimensions alone cannot authenticate a historical generation's backend or quality.

| GPT Image 2 modality | Input | Cached input | Output | Source, read date |
| --- | ---: | ---: | ---: | --- |
| Text prompt tokens | 5.00 | 1.25 | Not applicable | [OpenAI API pricing, Standard → All models](https://developers.openai.com/api/docs/pricing), 2026-10-26 |
| Image tokens | 8.00 | 2.00 | 30.00 | [OpenAI API pricing, Standard → All models](https://developers.openai.com/api/docs/pricing), 2026-10-26 |

The pricing page initially hides GPT Image 2 under **All models**. Its **Batch** image-output rate is 15.00, not the Standard rate of 30.00. Cached inputs apply only to the Responses API image tool, not direct Images API requests. [Pricing](https://developers.openai.com/api/docs/pricing) and [image guide](https://developers.openai.com/api/docs/guides/image-generation#cached-input-pricing), read 2026-10-26.

Published image-output prices depend on quality; the task supplies no quality metadata:

| Saved dimensions | Low | Medium | High | Status |
| --- | ---: | ---: | ---: | --- |
| 1024×1536 | 0.005 | 0.041 | 0.165 | Published rounded prices |
| 1536×1024 | 0.005 | 0.041 | 0.165 | Published rounded prices |
| 1672×941 | — | — | — | Exact price not published; dimensions violate API size rules |
| 1254×1254 | — | — | — | Exact price not published; dimensions violate API size rules |

Source for this table and the required multiples-of-16 size rule: [OpenAI image guide, earlier models and calculating costs](https://developers.openai.com/api/docs/guides/image-generation#calculating-costs), read 2026-10-26. No unique per-image price can be assigned without quality. `auto` does not specify one fixed tier. Input prompt/reference costs are additional.

For an explicitly approximate sensitivity calculation, the **same published model** is a better fallback than a sibling. The official calculator gives these nearby valid-size estimates; these are **proxies, not prices for the saved files**:

| Saved dimensions | Nearby valid proxy | Low | Medium | High |
| --- | --- | ---: | ---: | ---: |
| 1672×941 | 1680×944 | 0.00390 | 0.03486 | 0.13944 |
| 1254×1254 | 1248×1248 | 0.00684 | 0.06150 | 0.24591 |

Source: [OpenAI output-token calculator](https://developers.openai.com/api/docs/guides/image-generation#gpt-image-25-and-gpt-image-2-output-tokens), read 2026-10-26; estimates reproduced from its [published calculator code](https://developers.openai.com/_astro/GptImageTokenCalculator.react.Cf6ff7DM.js) at 30.00/M output tokens. Recover original generation size, quality, or billed usage for exact accounting; do not silently substitute these proxies. All requested model IDs have published rates, so no model-level sibling substitution is needed.

## Gemini Nano Banana 2.1 images at 2K

`gemini-nano-banana-2.1` Standard rates are **1.50 input**, **7.50 text/thinking output**, and **30.00 image output** per million tokens. A 2K image consumes 1,680 output tokens: **0.0504 per image**, plus prompt/reference and any text/thinking output. Batch is **0.0252 per 2K image**. [Google pricing](https://ai.google.dev/gemini-api/docs/pricing#gemini-nano-banana-21), read 2026-10-26.

Caching is **not supported**, so no cached-input tariff applies. The model has a 131,072-token input limit; no long-context price tier is published. [Google model specification](https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1), read 2026-10-26. This is Nano Banana **2.1**, not the older Nano Banana 2 (`gemini-3.1-flash-image`); its sibling's 2K price must not be substituted.

## Machine-readable rate card

The final block can be extracted as `prices.json`. Base `input`, `cached_input`, and `output` are Standard USD/M token rates. `per_image` values are USD/image, with quality keys where required. `null` means unavailable or unresolved, **never zero**. Empty `per_image` means no image-output tariff for that text model. GPT Image 2's base input/cache fields refer to **text**, its output field to **images**; Nano Banana's base output field refers to **text/thinking**. Additional modality and tier fields prevent conflating these rates. `proxy_per_image` is opt-in only. Do not charge both image tokens and a per-image equivalent for the same output.

For input totals that include cached input, the ordinary token subtotal is `(input_total - cached_input_tokens) * input / 1e6 + cached_input_tokens * cached_input / 1e6 + billed_output_tokens * output / 1e6`; separately account for cache writes and other modalities when present. Select long-context and speed tiers per request before summing a run.

```json
{
  "gpt-6.1-sol": {
    "input": 2.0,
    "cached_input": 0.1,
    "output": 10.0,
    "per_image": {},
    "cache_write_30m": 2.5,
    "cache_write_12h": 5.0,
    "long_context": { "input_gt": 272000, "input": 4.0, "cached_input": 0.2, "output": 15.0, "cache_write_30m": 5.0, "cache_write_12h": 10.0 },
    "speed_multipliers": { "fast": 2.0, "ultrafast": 6.0, "batch": 0.5, "flex": 0.5 },
    "source": "https://developers.openai.com/api/docs/models/gpt-6.1-sol",
    "cache_write_source": "https://developers.openai.com/api/docs/pricing",
    "read_date": "2026-10-26"
  },
  "gpt-5.6-sol": {
    "input": 4.0,
    "cached_input": 0.4,
    "output": 20.0,
    "per_image": {},
    "cache_write": 5.0,
    "long_context": { "input_gt": 272000, "input": 8.0, "cached_input": 0.8, "output": 30.0, "cache_write": 10.0 },
    "fast": { "input": 8.0, "cached_input": 0.8, "output": 40.0, "cache_write": 10.0 },
    "fast_long_context": { "input_gt": 272000, "input": 16.0, "cached_input": 1.6, "output": 60.0, "cache_write": 20.0 },
    "source": "https://cursor.com/docs/models/gpt-5-6-sol",
    "read_date": "2026-10-26"
  },
  "grok-4.7": {
    "input": 2.0,
    "cached_input": 0.5,
    "output": 6.0,
    "per_image": {},
    "long_context": { "input_gt": 256000, "input": 4.0, "cached_input": 1.0, "output": 12.0 },
    "fast": { "input": 4.0, "cached_input": 1.0, "output": 12.0 },
    "fast_long_context": { "input_gt": 256000, "input": 6.0, "cached_input": 1.5, "output": 18.0 },
    "source": "https://cursor.com/docs/models/grok-4-7",
    "read_date": "2026-10-26"
  },
  "gemini-4-argon": {
    "input": 2.0,
    "cached_input": 0.1,
    "output": 10.0,
    "per_image": {},
    "long_context": null,
    "valid_through": "2026-11-30",
    "from_2026_12_01": { "input": 4.0, "cached_input": 0.2, "output": 20.0 },
    "source": "https://ai.google.dev/gemini-api/docs/pricing#gemini-4-argon",
    "read_date": "2026-10-26"
  },
  "gpt-image-2": {
    "input": 5.0,
    "cached_input": 1.25,
    "output": 30.0,
    "input_modality": "text",
    "output_modality": "image",
    "image_input": 8.0,
    "cached_image_input": 2.0,
    "per_image": {
      "1672x941": null,
      "1024x1536": { "low": 0.005, "medium": 0.041, "high": 0.165 },
      "1536x1024": { "low": 0.005, "medium": 0.041, "high": 0.165 },
      "1254x1254": null
    },
    "proxy_per_image": {
      "1672x941": { "proxy_size": "1680x944", "low": 0.0039, "medium": 0.03486, "high": 0.13944 },
      "1254x1254": { "proxy_size": "1248x1248", "low": 0.00684, "medium": 0.0615, "high": 0.24591 }
    },
    "source": "https://developers.openai.com/api/docs/pricing",
    "per_image_source": "https://developers.openai.com/api/docs/guides/image-generation#calculating-costs",
    "model_identity_source": "https://learn.chatgpt.com/docs/image-generation",
    "read_date": "2026-10-26"
  },
  "gemini-nano-banana-2.1": {
    "input": 1.5,
    "cached_input": null,
    "output": 7.5,
    "output_modality": "text_and_thinking",
    "image_output": 30.0,
    "per_image": { "2K": 0.0504 },
    "batch_per_image": { "2K": 0.0252 },
    "caching_supported": false,
    "source": "https://ai.google.dev/gemini-api/docs/pricing#gemini-nano-banana-21",
    "read_date": "2026-10-26"
  }
}
```

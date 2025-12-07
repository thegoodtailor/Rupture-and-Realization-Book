# Chapter 7 — Names as Corecursive Trajectories (names‑first cut)

**Slogan.** A *name* is a trajectory‑in‑motion whose meaning is *witnessed* at every beat. Each inference step is a tick of logical time; coherence is the film that keeps running.

## Motivation: the projection room
Think of the projection booth. The reel is a becoming: cuts, pans, rewinds, splices. A name is not a token at one instant; it is a **kept motion**. If the scene jumps (a rupture), we do not lose the character because an explicit bridge—our coherence witness—carries identity across the cut.

**Scope.** We stay inside DHoTT at a fixed world. No agency, no Grothendieck yet. The goal: define and analyze **names** as corecursive witnesses of meaning over time.

## Light DHoTT recap
- Time index/category: **T**.
- Evolving type (presheaf): `A : Tᵒᵖ → U`.
- Trajectory from τ: `α : ∏_{t≥τ} A(t)`.
- Coherence along a step `(t→t′)` is a DHoTT term `Coh(t→t′, α(t), α(t′))` (transport / drift / repair as in Ch. 6).
- Choose a small basis **E** of steps; check coherence on generators and close under composition.

**Robust coherence**
```
R⋆(α)  ≔  ∏_{(t→t′)∈E, τ≤t≤t′} Coh(t→t′, α(t), α(t′))
       ≃  ν X. ( Coh(t→next(t), α(t), α(next(t))) × ▷ X )
```
(Guarded form using the later modality ▷.)

## Names as corecursive witnesses
```
Name(A, τ) ≔ Σ_{α : ∏_{t≥τ} A(t)}  R⋆(α)
```
A name is a pair `(α, ρ)` where `ρ` is the recursive reel of coherence proofs.

- **Meaning as kept motion.** A lone inhabitant `a ∈ A(τ)` is only a term‑now. A name is the *kept trajectory* with witnesses at every cut.

### Transport invariance
If `A(t) ≃ B(t)` naturally in `t`, then `Name(A, τ) ≃ Name(B, τ)` (by transport; univalence if desired).

### Basis independence (idea)
Witnesses on generators extend to all intervals by composition; different editing bases choose an *editing tempo*, not a different notion of name.

## Film‑room interpretation
- **Pan (adiabatic drift):** `Coh` is carried by transport.
- **Jump cut (rupture):** add an explicit repair witness (a new establishing shot). The character persists because the projectionist supplies the reel `ρ`.

## Elementary constructions
- **Restriction:** start later by tailing the trajectory and witnesses.
- **Re‑typing under soft change:** internal equivalences let us switch stock without loss.
- **Observation maps:** any fibrewise `f : A → B` gives `f_* : Name(A, τ) → Name(B, τ)`.

## What we defer (and why)
Non‑equivalence context change, Grothendieck indexing, and **agents** (generativity/worlds) are Chapter 10’s business. Here: **name = robust, corecursively witnessed trajectory**.

## Checklist
- Equivalence invariance ✔︎
- Basis independence (sketch; full proof later)
- Closure under fibrewise maps ✔︎
- Stability under guarded limits (coinduction; later)
- Rupture/heal rules: admissible `Coh` witnesses suffice here; full syntax/semantics in Ch. 6.

**One‑line moral.** *Name = trajectory + a reel of coherence proofs that never runs out.*

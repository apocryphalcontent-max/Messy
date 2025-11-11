# Subject Pool Generation for Opus Maximus

This directory contains the complete 14,500+ subject queue for generating Orthodox Christian theological entries.

## Files

### `subject_pool_14500_complete.json` (5.8 MB)
**Complete subject pool with 16,219 subjects** across 11 theological categories.

This is the production-ready queue for the Opus Maximus generation system.

### `generate_subject_pool.py`
Python script that generates the complete subject pool programmatically.

Can be modified to:
- Adjust category distributions
- Add new subject categories
- Change difficulty assessments
- Modify tier assignments

## Subject Pool Statistics

**Total Subjects:** 16,219

### Category Distribution:
- **Systematic Theology:** 2,490 subjects
  - Trinity, Theosis, Grace, Salvation, Church, Sacraments, Eschatology, Anthropology
- **Patristic Theology:** 1,499 subjects
  - Apostolic Fathers, Pre-Nicene, Cappadocian, Alexandrian, Byzantine, Modern Saints
- **Dogmatic Theology:** 1,980 subjects
  - Creeds, Councils, Christology, Trinitarian doctrine, Iconography
- **Liturgical Theology:** 1,650 subjects
  - Divine Liturgy, Sacraments, Holy Week, Festal cycle, Hymnography
- **Ascetical Theology:** 1,300 subjects
  - Prayer, Fasting, Hesychasm, Virtues, Spiritual warfare, Monasticism
- **Moral Theology:** 1,000 subjects
  - Ethics, Social teaching, Bioethics, Family life
- **Historical Theology:** 1,300 subjects
  - Church history periods, councils, schisms, martyrs
- **Biblical Theology:** 1,000 subjects
  - OT/NT theology, Septuagint, Orthodox exegesis
- **Biographical:** 1,500 subjects
  - Saints across all eras and regions
- **Advanced Thinkers:** 1,000 subjects
  - Philosophers, theologians, converts, apologists
- **Divine Manifestations:** 1,500 subjects
  - Miracles, apparitions, relics, supernatural events

### Quality Tiers:
- **Tier 1:** 2,000+ foundational subjects (highest priority, most complex)
- **Tier 2:** 7,000+ intermediate subjects
- **Tier 3:** 7,000+ advanced specialized subjects

### Difficulty Distribution:
- **Difficulty 10** (Extremely Complex): Trinity, Hypostatic Union, Divine Energies, Filioque
- **Difficulty 8-9** (Very Complex): Christology, Theosis, Major Church Fathers
- **Difficulty 6-7** (Complex): Sacraments, Councils, Monasticism
- **Difficulty 4-5** (Moderate): Saints, Liturgical practices, Ethics

## Usage

### Generate Fresh Subject Pool
```bash
python3 generate_subject_pool.py
```

### Use in Opus Maximus System
```python
import json

# Load subject pool
with open('subject_pool_14500_complete.json', 'r') as f:
    pool = json.load(f)

# Access subjects
subjects = pool['subjects']
metadata = pool['metadata']

# Filter by category
systematic = [s for s in subjects if s['category'] == 'Systematic Theology']

# Filter by tier
tier1 = [s for s in subjects if s['tier'] == 'Tier 1']

# Sort by priority
priority_queue = sorted(subjects, key=lambda x: x['priority'])
```

### Subject Structure

Each subject contains:
```json
{
  "id": 1,
  "name": "The Holy Trinity",
  "category": "Systematic Theology",
  "tier": "Tier 1",
  "difficulty": 10,
  "keywords": ["Trinity", "Father", "Son", "Holy Spirit"],
  "prerequisites": [],
  "related": ["Divine Essence", "Perichoresis"],
  "estimated_time_minutes": 45,
  "priority": 1
}
```

## Generation Estimates

### Time Estimates:
- **Average per entry:** 30-35 minutes (with warm cache)
- **Daily output (24/7):** 40-50 entries
- **Total time:** 325-400 days for complete corpus

### Quality Targets:
- **100% CELESTIAL tier** (score ≥95)
- **20+ Patristic citations** per entry
- **15+ Scripture references** per entry
- **12,000+ words** per entry minimum

## Integration with Master Generation Guide

This subject pool integrates with the specifications in `MASTER_GENERATION_GUIDE.md`:

1. **Preprocessing Pipeline** - Use subject pool for relationship mapping, cross-reference generation
2. **Batch Processor** - Feed subjects in priority order for optimal cache efficiency
3. **Quality Validator** - Each subject includes difficulty for model selection
4. **Progress Tracking** - 16,219 total subjects for completion metrics

## Customization

To add new subjects or modify the pool:

1. Edit `generate_subject_pool.py`
2. Add new categories or expand existing ones
3. Run script to regenerate `subject_pool_14500_complete.json`
4. Validate with:
   ```python
   pool = json.load(open('subject_pool_14500_complete.json'))
   print(f"Total: {pool['metadata']['total_subjects']}")
   print("Categories:", pool['metadata']['categories'])
   ```

## Next Steps

1. **Run preprocessing pipeline** on this subject pool (saves 220-404 hours)
2. **Start batch generation** beginning with Tier 1 priority subjects
3. **Monitor progress** through dashboard or CLI
4. **Track quality** - ensure all entries meet CELESTIAL tier standards

---

**Generated:** 2024  
**Version:** 1.0  
**Target:** 14,500+ CELESTIAL-tier Orthodox Christian theological entries  
**Cost:** $0 (100% local generation)

from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from api.public.community.models import Community

class Subregion(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100, unique=True, index=True)
    area: Optional[float] = Field(default=None, description="Area in square kilometers")
    population: Optional[int] = Field(default=None, description="Population")
    borders: Optional[str] = Field(default=None, description="List of bordering divisions")
    capital: Optional[str] = Field(default=None, description="Capital or main city")
    website: Optional[str] = Field(default=None, description="Official website")
    head_of_government: Optional[str] = Field(default=None, description="Current head of government")
    head_of_government_title: Optional[str] = Field(default=None, description="Title of head of government")
    community_id: int = Field(foreign_key="community.id")
    region_id: Optional[int] = Field(default=None, foreign_key="region.id")

    # Relationships
    community: Community = Relationship(back_populates="subregion")
    region: Optional["Region"] = Relationship(back_populates="subregions")
    localities: list["Locality"] = Relationship(back_populates="subregion")
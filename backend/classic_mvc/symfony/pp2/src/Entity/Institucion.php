<?php

namespace App\Entity;

use App\Repository\InstitucionRepository;
use Doctrine\Common\Collections\ArrayCollection;
use Doctrine\Common\Collections\Collection;
use Doctrine\ORM\Mapping as ORM;

#[ORM\Entity(repositoryClass: InstitucionRepository::class)]
class Institucion
{
    #[ORM\Id]
    #[ORM\GeneratedValue]
    #[ORM\Column]
    private ?int $id = null;

    #[ORM\Column(length: 100)]
    private ?string $nombre = null;

    #[ORM\Column(length: 50)]
    private ?string $direccion = null;

    #[ORM\Column(length: 15)]
    private ?string $telefono = null;

    #[ORM\Column(length: 100)]
    private ?string $email = null;

    #[ORM\OneToMany(targetEntity: Personal::class, mappedBy: 'institucion')]
    private Collection $personals;

    public function __construct()
    {
        $this->personals = new ArrayCollection();
    }

    public function getId(): ?int
    {
        return $this->id;
    }

    public function getNombre(): ?string
    {
        return $this->nombre;
    }

    public function setNombre(string $nombre): static
    {
        $this->nombre = $nombre;

        return $this;
    }

    public function getDireccion(): ?string
    {
        return $this->direccion;
    }

    public function setDireccion(string $direccion): static
    {
        $this->direccion = $direccion;

        return $this;
    }

    public function getTelefono(): ?string
    {
        return $this->telefono;
    }

    public function setTelefono(string $telefono): static
    {
        $this->telefono = $telefono;

        return $this;
    }

    public function getEmail(): ?string
    {
        return $this->email;
    }

    public function setEmail(string $email): static
    {
        $this->email = $email;

        return $this;
    }

    /**
     * @return Collection<int, Personal>
     */
    public function getPersonals(): Collection
    {
        return $this->personals;
    }

    public function addPersonal(Personal $personal): static
    {
        if (!$this->personals->contains($personal)) {
            $this->personals->add($personal);
            $personal->setInstitucion($this);
        }

        return $this;
    }

    public function removePersonal(Personal $personal): static
    {
        if ($this->personals->removeElement($personal)) {
            // set the owning side to null (unless already changed)
            if ($personal->getInstitucion() === $this) {
                $personal->setInstitucion(null);
            }
        }

        return $this;
    }
    public function __toString(){
        return $this->nombre;
    }
}
